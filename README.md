# MProb — Notas de Aula de Métodos Probabilísticos

Notas de aula da disciplina **Métodos Probabilísticos**, do curso de
Meteorologia da **Universidade de Brasília (UnB)**.

## Conteúdo

- `sup-inf.tex` — documento principal (fonte única), com preâmbulo e chamadas aos capítulos.
- `capitulos/` — capítulos do material, um arquivo `.tex` por capítulo.
- `arquivos-aux/` — artefatos de apoio: logos institucionais, template de notas, referências bibliográficas.

## Compilação

O documento principal é `sup-inf.tex`. A forma mais simples de compilar é com `latexmk`:

```bash
latexmk -pdf sup-inf.tex
```

O PDF final sai em `sup-inf.pdf`.

## Estrutura

```
.
├── sup-inf.tex            # documento principal
├── capitulos/
│   ├── capitulo1.tex
│   └── capitulo2.tex
└── arquivos-aux/
    ├── referencias.bib
    ├── template-notas.tex
    └── logos/figuras institucionais
```

## Licença

Material didático de livre uso. Ao citar ou reutilizar, mencione a origem e o autor.
