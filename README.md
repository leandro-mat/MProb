# MProb — Notas de Aula de Métodos Probabilísticos

Notas de aula da disciplina **Métodos Probabilísticos**, do curso de
Meteorologia da **Universidade de Brasília (UnB)**.

## Estrutura

O repositório é organizado como **um diretório por nota de aula**. Cada
subpasta contém seu próprio `.tex` principal e seus capítulos. Os recursos
compartilhados (logo da UnB, referências, template) ficam uma única vez em
`arquivos-aux/` e são referenciados de cada nota via caminho relativo
(`../arquivos-aux/...`). Assim, com 40 notas de aula existe apenas uma cópia
da figura do cabeçalho e do `.bib`.

```
.
├── sup-inf/                      # nota de aula (exemplo)
│   ├── sup-inf.tex               # documento principal da nota
│   ├── capitulos/
│   │   ├── capitulo1.tex
│   │   └── capitulo2.tex
│   └── sup-inf.pdf               # PDF compilado
├── <proxima-nota>/               # futuras notas seguem o mesmo padrão
│   └── <proxima-nota>.tex
└── arquivos-aux/                 # compartilhado por todas as notas
    ├── referencias.bib
    ├── template-notas.tex        # ponto de partida para novas notas
    └── logos/figuras institucionais
```

## Criando uma nova nota

1. Copie `arquivos-aux/template-notas.tex` para dentro de uma nova subpasta.
2. Renomeie o arquivo e ajuste título, autor, data, resumo e conteúdo.
3. O template já aponta para os recursos compartilhados (`../arquivos-aux/`),
   inclusive a figura do cabeçalho e a bibliografia — nada precisa ser copiado.

## Compilação

Dentro da subpasta da nota, compile com `latexmk`:

```bash
latexmk -pdf sup-inf.tex
```

O PDF final sai na própria subpasta (ex.: `sup-inf/sup-inf.pdf`).

## Licença

Material didático de livre uso. Ao citar ou reutilizar, mencione a origem e o autor.
