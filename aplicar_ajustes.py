#!/usr/bin/env python3
r"""
Aplica os ajustes de capa (ppg-ieee.cls) e do \pendente (thesis.tex).

Uso (dentro da pasta do projeto):
    python3 aplicar_ajustes.py packages/ppg-ieee.cls thesis.tex

Faz cópia de segurança (.bak) antes de alterar e para com erro se algum
trecho esperado não for encontrado (nada é gravado nesse caso).
"""
import re, shutil, sys

def ler(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def gravar(p, t):
    shutil.copyfile(p, p + ".bak")
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)

def trocar_uma_vez(t, antigo, novo, rotulo):
    if t.count(antigo) != 1:
        sys.exit(f"ERRO: '{rotulo}' encontrado {t.count(antigo)}x (esperado 1x). Nada foi alterado.")
    return t.replace(antigo, novo)

def trocar_regex(t, padrao, novo, rotulo):
    t2, n = re.subn(padrao, lambda m: novo, t, count=1, flags=re.S)
    if n != 1:
        sys.exit(f"ERRO: bloco '{rotulo}' não encontrado. Nada foi alterado.")
    return t2

TITULO = r"""\begin{textblock*}{\capalargura}(\capax,65mm)%
      \begin{fittext}
        \raggedright%
        \textcolor{blue-capa}{
          \nohyphens{\imprimirtitulo}
        }
      \end{fittext}
    \end{textblock*}%"""

AUTOR = r"""\begin{textblock*}{\capalargura}(\capax,123mm)%
      \noindent
      \begin{minipage}[t][65mm][t]{\capalargura}
        \begin{otherlanguage}{brazil}
          \begin{SingleSpace}
            \linespread{1.0}%
            \begin{flushleft}
              \nohyphens{%
                \color{blue-capa}%
                {\color{blue-capa}\rule{40mm}{1.2pt}}\par\vspace{4mm}%
                \maxsizebox{\capalargura}{5mm}{\@icmcAutorCapa\imprimirautor}%

                \vspace{3mm}%

                \ifthenelse{\boolean{opt-qualificacao}}{%
                    \@ppgPrograma Qualifica{\c c}{\~a}o de \tipodocurso~do \imprimirprograma~(\imprimirsiglaprograma)%
                }{%
                    \@ppgPrograma\imprimirtipotrabalho~de \tipodocurso~do \imprimirprograma~(\imprimirsiglaprograma)%
                }%

              }
            \end{flushleft}
          \end{SingleSpace}
        \end{otherlanguage}
      \end{minipage}
    \end{textblock*}%"""

PENDENTE = (r"\newcommand{\pendente}[1]{\ifmostrarnotas" "\n"
            r"  \par\noindent\colorbox{yellow!60}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\raggedright #1}}\par" "\n"
            r"  \else #1\fi}")

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    cls_path, tex_path = sys.argv[1], sys.argv[2]
    cls, tex = ler(cls_path), ler(tex_path)

    # ---- classe ----
    if r"\begin{minipage}{\capalargura}%" in cls:
        sys.exit("Os ajustes da classe já foram aplicados. Nada a fazer.")
    if r"\newlength{\capalargura}" not in cls:
        cls = trocar_uma_vez(
            cls, r"\NewEnviron{fittext}",
            "\\newlength{\\capalargura}\\setlength{\\capalargura}{125mm}\n"
            "\\newcommand{\\capax}{70mm}\n\n\\NewEnviron{fittext}", r"\NewEnviron{fittext}")
    cls = trocar_uma_vez(cls, r"\begin{minipage}{144mm}%",
                         r"\begin{minipage}{\capalargura}%", "minipage de medição (144mm)")
    cls = trocar_uma_vez(cls, r"\begin{minipage}[c][47mm][c]{144mm}",
                         r"\begin{minipage}[c][47mm][c]{\capalargura}", "minipage final (144mm)")
    cls = trocar_regex(cls, r"\\begin\{textblock\*\}\{144mm\}\(61mm,65mm\)%.*?\\end\{textblock\*\}%",
                       TITULO, "bloco do título da capa")
    cls = trocar_regex(cls, r"\\begin\{textblock\*\}\{130mm\}\(81mm,123mm\)%.*?\\end\{textblock\*\}%",
                       AUTOR, "bloco do autor da capa")

    # ---- thesis.tex ----
    tex = re.sub(r"^\\makeatletter\\@namedef\{ver@natbib\.sty\}.*\\makeatother[ \t]*\n\n?", "", tex, flags=re.M)
    tex = trocar_uma_vez(
        tex, r"\newcommand{\pendente}[1]{\ifmostrarnotas\colorbox{yellow!60}{#1}\else #1\fi}",
        PENDENTE, r"definição de \pendente")

    gravar(cls_path, cls)
    gravar(tex_path, tex)
    print("OK. Cópias de segurança: %s.bak e %s.bak" % (cls_path, tex_path))

main()
