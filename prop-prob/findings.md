# Findings & Decisions — Diagramas TikZ

## Requisitos
- 6 diagramas nos locais apropriados de `prop-prob.tex`.
- Estilo do documento: `line width=0.7pt`, padrões `north west/east lines`,
  cores sóbrias (preto/cinza; `teal` definida no preâmbulo), captions em pt-BR.
- Pacotes disponíveis: tikz (libraries: positioning, calc, fit, patterns,
  decorations.pathreplacing, calligraphy, tikzmark, nfold), pgfplots 1.17,
  fontawesome5 (ícones de dado).
- NÃO usar a palavra "independência" em nenhum texto novo (conceito ainda
  não introduzido no curso).

## Âncoras de inserção (trechos exatos no .tex)

### Fig 4 — `fig:demorgan` (seção 2)
- Âncora: parágrafo que contém
  `\[ \Omega \setminus (A \cap B) = (\Omega \setminus A) \cup (\Omega \setminus B) \]`
- Edição textual: acrescentar "como ilustra a \Cref{fig:demorgan}" após
  "…\(A\) não ocorre ou \(B\) não ocorre''."
- Inserir figure após o fim desse parágrafo (antes de "Essa correspondência sugere").
- Design: 2 painéis lado a lado (shifts ±2.35). Retângulo Ω = (-1.9,-1.2) a
  (1.9,1.2); círculos A centro (-0.55,0) r 0.95, B centro (0.55,0) r 0.95.
  - Esquerda: padrão NW em tudo; lente A∩B branca (clip A + fill B branco);
    labels A (-1.2,0.45), B (1.2,0.45), A∩B (0,0); abaixo: Ω∖(A∩B).
  - Direita: padrão NW em Ω∖A (fill retângulo + fill A branco); depois
    clip A + padrão NE no retângulo + fill B branco → A∖B com padrão 2;
    labels A∖B (-1.2,0.45), Ω∖A (1.2,0.45), A∩B (0,0);
    abaixo: (Ω∖A)∪(Ω∖B).
  - Labels sobre padrão: `fill=white, inner sep=1pt`.

### Fig 3 — `fig:atomos` (seção 2, após ex:1.7)
- Âncora: fim do ambiente ex:1.7 ("…descrições de resultados.\n\end{example}").
- Edição textual: frase final no ex:1.7 remetendo à \Cref{fig:atomos}.
- Design: Ω retângulo arredondado (-3.9,-2.5) a (3.9,1.9). Três blocos
  (fill black!6): bloco1 (-3.3,0.15)-(-0.6,1.35) com \faDiceOne\faDiceTwo;
  bloco3 (0.6,0.15)-(3.3,1.35) com \faDiceFive\faDiceSix;
  bloco2 (-1.35,-1.95)-(1.35,-0.75) com \faDiceThree\faDiceFour.
  Evento A: dois retângulos tracejados (line width 0.9pt) ao redor dos
  blocos 1 e 3 (folga ~0.15), label \(A\) em (0,1.72).
- Caption: partição de Ω do ex:1.7; cada evento é união de blocos; destaque
  A = {⚀,⚁,⚄,⚅} (escrever com \text{\faDiceOne} etc.).

### Fig 1 — `fig:telescopia` (seção 6)
- Âncora: prova do thm:1.54; substituir "(desenhe um diagrama de Venn para
  tornar isso claro)" por "(veja a \Cref{fig:telescopia})". Inserir figure
  logo após `\end{proof}`.
- Design: círculos concêntricos r=0.6 (A_1, fill black!15), 1.05 (A_2),
  1.5 (A_3), 2.1 tracejado (A, fill black!8 por baixo). Labels na vertical:
  A_1 (0,0.25), B_2 (0,0.83), B_3 (0,1.28), B_4∪B_5∪⋯ (0,1.8).
  Labels dos círculos no raio -45°: A_2 (0.78,-0.78), A_3 (1.1,-1.1),
  A (1.55,-1.55), todos fill=white. Faixa abaixo:
  \(A_1 \subseteq A_2 \subseteq A_3 \subseteq \cdots \subseteq A = \bigcup A_i\) em (0,-2.7).

### Fig 5 — `fig:arvore-moeda` (seção 6, após ex:1.55)
- Âncora: fim do ex:1.55 ("…é igual a 0.\n\end{example}"). Acrescentar frase
  remetendo à \Cref{fig:arvore-moeda}; figure após \end{example}.
- Design: árvore MANUAL (coordenadas explícitas, evitar surpresas de sintaxe
  de tree). scale=0.85. root (0,0) ponto preenchido; nível 1 y=-1.5:
  C=(-2.8), K=(2.8); nível 2 y=-3: CC=-4.2, CK=-1.4, KC=1.4, KK=4.2;
  nível 3 y=-4.5: CCC=-4.9, CCK=-3.5, CKC=-2.1, CKK=-0.7, KCC=0.7,
  KCK=2.1, KKC=3.5, KKK=4.9. Nós círculo draw, conteúdo sequência.
  Labels de aresta: `node[midway, sloped, above]{\footnotesize C/K}`.
  Destaque (fill black!25, edge line width 1.2pt): r→K→KK→KKK.
  Abaixo de K, KK, KKK: probabilidades 1/2, 1/4, 1/8 (\tfrac).
  De KKK aresta tracejada até (4.9,-5.7) com \vdots.
- Caption: caminho destacado = nunca obter cara; prob. até nível n é 2^{-n}→0.

### Fig 2 — `fig:zeta-massas` (seção 5, após ex:zeta)
- Âncora: fim do ex:zeta ("…como lei de Zipf.\n\end{example}"); inserir
  figure após \end{example} (antes de "Há uma fatoração instrutiva").
- Edição textual: após "e a probabilidade de obter um número par é 1/4."
  acrescentar "(veja a \Cref{fig:zeta-massas})".
- Design: pgfplots ybar, s=2, n=1..12. Valores p_n = 6/(π²n²):
  (1,0.6079)(2,0.1520)(3,0.0676)(4,0.0380)(5,0.0243)(6,0.0169)
  (7,0.0124)(8,0.0095)(9,0.0075)(10,0.0061)(11,0.0050)(12,0.0042)
  Dois \addplot: ímpares fill black!25, pares fill black!70; legend.
  Axis: width=0.85\textwidth, height=5.2cm, ymin=0, ymax=0.68,
  xtick 1..12, yticklabel fixed precision 2.
- Caption: massas da zeta com s=2; barras escuras = pares; soma = 1/4.

### Fig 6 — `fig:crivo-euler` (seção 5, após prova da prop:euler)
- Âncora: fim da prova da prop:euler ("…que é o resultado desejado.\n\end{proof}"),
  antes do parágrafo "Em termos do espaço do \Cref{ex:zeta}".
- Edição textual: na prova, após a definição de S_N, acrescentar
  "(veja a \Cref{fig:crivo-euler})".
- Design: grade 10×3 (números 1..30), scale=0.75. Célula do n:
  col=mod(n-1,10), row=int((n-1)/10), retângulo (col,-row)+ +(1,1).
  Ordem: fills brancos → fills teal!25 nos 3-suaves
  {1,2,3,4,6,8,9,12,16,18,24,27} → `\draw (0,0) grid (10,-3);` → números.
- Caption: S_3 entre 1 e 30 = números da forma 2^a 3^b; todo n≤3 pertence a
  S_3; cada inteiro fixado entra em S_N para N grande.

## Convenções do arquivo (verificado)
- Ambientes theorem/definition/example/proposition compartilham contador
  (aliascnt); exercise tem contador próprio.
- Referências sempre via \Cref/\cref (cleveref brazilian, nameinlink).
- Compilar: `latexmk -pdf -interaction=nonstopmode -halt-on-error prop-prob.tex`
  no diretório prop-prob/. Warnings pré-existentes a ignorar: doclicense
  "No language definition for brazil", "Empty thebibliography".
- Gráficos: `\graphicspath{{./}{../arquivos-aux/}}`; logo já funciona.

## Issues
| Issue | Resolution |
|-------|------------|
| Usuário edita o .tex em paralelo (frases retrabalhadas, numeração de exemplos mudou: ex:zeta = "Exemplo 12", ex:1.7 = "Exemplo 5" etc.) | Sempre re-grep/re-ler a região antes de editar; âncoras de `findings.md` podem estar desatualizadas — confiar nos labels, não nos números |
| `fixed zerofixed` não existe no pgfplots | usar `/pgf/number format/fixed` + `precision=2` |
| Figura pgfplots larga demais (overfull 12.6pt) | width ≤ 0.85\textwidth |
| Rótulos com fill=white colidem quando alinhados na mesma linha | deslocar verticalmente (y=-0.4) |
