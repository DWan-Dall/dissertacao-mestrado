Modelo de Teses e Dissertações 

Este modelo visa atender às exigências dos Programas de Pós-Graduação do Instituto de Ciências Matemáticas e de Computação. As normas principais estão baseadas na ABNT, com algumas adaptações em relação aos estilos dos capítulos, capa e folhas de rosto.

O requisito básico para utilização da classe **_ppg_** é criar um documento desta classe com o comando
`\documentclass[@parameters]{ppg}` e ter, no diretório de trabalho, o arquivo *ppg.cls* presente. Entretanto, recomenda-se fortemente manter a estrutura de diretório inicial fornecida por este modelo. 

Para que o documento esteja em conformidade com as normas exigidas pelo programa de Pós-Graduação, o **projeto deve ser compilado utilizando *XeLaTeX* ou *LuaLaTeX***. Esse processo de compilação é necessário para que as fontes externas utilizadas para gerar a capa sejam incluídas.

Os parâmetros possíveis utilizados pelo `\documentclass` são:
- **[qualificacao]** Exclusivamente para monografias de qualificação em geral;
- **[mestrado / doutorado]** Identifica o curso ao qual o aluno pertence, sendo utilizado apenas uma das duas opções disponíveis. O valor padrão é **doutorado**;
- **[pre-defesa / pos-defesa]** Identifica a situação do documento (exceto para qualificação), sendo necessário apenas uma das duas opções. O valor padrão é **pos-defesa**;
- **[impressao]** Gera exclusivamente uma versão para impressão do documento;
- **[french, spanish, english, brazil]** Adiciona o idioma para correta hifenização no documento. Os idiomas bases para o modelo (português e inglês) não precisam ser declarados.

Para compilação utilizar o comando:
```
latexmk -lualatex -interaction=nonstopmode -file-line-error thesis.tex
```