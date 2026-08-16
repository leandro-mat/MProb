# Task Plan: Diagramas TikZ para prop-prob.tex

## Goal
Inserir 6 diagramas TikZ/pgfplots em `prop-prob/prop-prob.tex` nos locais
apropriados (especificações em `findings.md`), compilando sem erros, sem
overfull boxes relevantes e sem referências indefinidas.

## Current Phase
Phase 3 (verificação) — complete; tarefa concluída em 1 sessão.

## Phases

### Phase 1: Especificação e planejamento
- [x] Identificar locais e desenhar especificação de cada figura
- [x] Documentar em `findings.md`
- **Status:** complete

### Phase 2: Implementação (ordem escolhida)
- [x] Fig 4 `fig:demorgan` — leis de De Morgan (seção 2)
- [x] Fig 3 `fig:atomos` — partição/átomos da σ-álgebra (após ex:1.7)
- [x] Fig 1 `fig:telescopia` — sequência crescente fatiada (seção 6)
- [x] Fig 5 `fig:arvore-moeda` — árvore de lançamentos (após ex:1.55)
- [x] Fig 2 `fig:zeta-massas` — barras da distribuição zeta (após ex:zeta)
- [x] Fig 6 `fig:crivo-euler` — grade S_N (após prova da prop:euler)
- **Status:** complete

### Phase 3: Verificação final
- [x] Compilação limpa (2 passadas p/ cleveref)
- [x] Sem warnings novos no log
- [x] Inspeção visual das 6 páginas (pdftoppm)
- [x] Atualizar `progress.md`
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Labels descritivos (`fig:zeta-massas` etc.) | numeração de teoremas já é deslocada dos nomes de label; \Cref resolve |
| Figuras `[htbp]` | padrão do documento |
| Compilar com `latexmk -pdf` a cada lote de 2 figuras | detectar erros de TikZ cedo |
| Arquivos .md são notas de trabalho NÃO versionadas | repo é material didático público |
| Ícones de dado via `\faDiceOne`... (fontawesome5 já carregado) | consistência com ex:1.7 |
| pgfplots para barras (já carregado, compat=1.17) | evitar desenho manual |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       |         |            |

## Notes
- Commit local já feito ANTES desta tarefa: `cd9a623` (zeta + Euler).
- Não fazer push sem pedido explícito.
- Ao retomar em outra sessão: ler este arquivo + `findings.md` + `progress.md`.
