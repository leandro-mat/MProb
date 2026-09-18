# Parecer de revisão — `func-distribuicao.tex`

**Arquivo revisado:** `/Users/cioletti/Documents/MProb/func-distribuicao/func-distribuicao.tex` (2296 linhas)
**Data:** 17/09/2026
**Escopo:** revisão ortográfica/gramatical (PT-BR) + auditoria matemática e de rigor. Preâmbulo (linhas 1–267) fora do escopo, exceto quando afeta o texto.
**Método:** dois subagentes em paralelo — `ds-flash` (ortografia/estilo) e `luna` (matemática) — com relatórios integrais em `agent-output/revisao-ortografica.md` (120 linhas) e `agent-output/revisao-matematica.md` (43 linhas).
**Ação tomada:** nenhum byte do `.tex` foi alterado, conforme solicitado. Este `parecer.md` é o único arquivo novo na raiz; os relatórios brutos permanecem em `agent-output/` para consulta.

## Veredito global

Texto matematicamente sólido e bem escrito. Há **1 erro ortográfico inequívoco**, ~15 correções gramaticais pontuais e ~12 pontos de uniformidade de estilo. Na matemática, **nenhum teorema central está errado** (FD, densidades usuais, beta–gama, Cantor, exercícios principais estão corretos, inclusive colagens em $1/3$, $2/3$ e constantes de normalização), mas há **3 pontos que exigem decisão/correção antes de publicar** (hipótese “contínua” vs. “absolutamente contínua”, descompasso Borel/Lebesgue no TCD, enunciado incompleto do arco-seno) e 2 complementos de prova recomendados (convergência uniforme/Banach, preservação de monotonicidade). Todo o resto é sugestão de clareza.

---

## A. Ortografia, gramática e estilo (fonte: `agent-output/revisao-ortografica.md`)

### A1. Erro ortográfico certo (corrigir)

- [L1648] `a raíz quadrada` → `a raiz quadrada` — “raiz” é paroxítona sem acento.

### A2. Gramática/pontuação (recomendado corrigir)

- [L973–974] `A sequência de funções definida recursivamente acima, converge uniformemente` → remover vírgula (sujeito–verbo).
- [L806–807] `Quando uma variável aleatória é absolutamente contínua a identidade …` → `… contínua, a identidade …` (falta vírgula).
- [L841] `Desta forma a função` → `Desta forma, a função`.
- [L1369–1370] `… do cálculo integral é necessário …` → vírgula após `integral`.
- [L1646] `Como veremos mais à frente o parâmetro …` → `… à frente, o parâmetro …`.
- [L1458] `… \mathds{1}_{I}(x)$, para quase todo $x$` → retirar vírgula antes de `para`.
- [L813–814] `Uma boa parte dos textos … chamam` → `chama` (sujeito singular).
- [L788] `… classe … que chamaremos de \emph{absolutamente contínua}` → `… cujos elementos chamaremos de \emph{absolutamente contínuos}` (é a variável, não a classe, que é contínua).
- [L1402] `a grosso modo` → `grosso modo` (locução latina sem artigo/crase).
- [L1527] `em uma variável aleatória contínua` → `para uma variável aleatória contínua` (regência).
- [L922–923] `são chamadas de singulares contínuas` → `são chamadas de variáveis singulares contínuas` (ou `são ditas singulares contínuas`).
- [L1394] `são as análogas de …` vs. [L1381] `análogo ao` → uniformizar regência (`análogas a`).
- [L1512] `Como $\{X=a\}$ tem probabilidade $0$ por hipótese` → `pela primeira parte` (não é hipótese, é consequência de \eqref{eq:prob-ponto}).
- [L1907] `Para todos $s>0$ e $t>0$ vale` → `Para todo $s>0$ e todo $t>0$ vale` (ou `Para quaisquer $s,t>0$`).
- [L1878] `Não é sempre trivial verificar` → `Nem sempre é trivial verificar`.
- [L1396–1397] `No exemplo exponencial, por exemplo` → redundância; cortar um dos dois.
- [L417–418] `toda variável aleatória discreta é uma variável aleatória no sentido mais amplo` → `é também uma variável aleatória no sentido amplo` (repetição).

### A3. Imprecisões de redação que tocam o enunciado matemático

- [L554–555] `o evento de que $X$ seja menor do que $x$` descreve $\{X<x\}$, não $\{X\leqslant x\}$ → `o evento de que $X$ não exceda $x$`.
- [L522] `suas assíntotas horizontais existem` → `seus limites em $-\infty$ e $+\infty$ existem` (limite no infinito não é “assíntota”).
- [L560–562] `$\mathbb{P}(X\leqslant-\infty)=0$` — notação sugestiva mas abusiva; considerar reescrita ou comentário explícito de que é intuição, não definição.
- [L1469–1470] `Se $X$ é contínua com densidade $f_X$` → `Se $X$ é absolutamente contínua …` (ver §B; conflita com a distinção da própria Seção 3).
- [L1185–1187] `A notação “com probabilidade $1$” enfatiza que o ponto escolhido está em $\mathbb{K}$ sem exceção relevante` — frase contraditória (prob. 1 = q.c., mas a inclusão é certa por construção); reformular explicando a ênfase.

### A4. Uniformidade global (decisão editorial sua; lista completa no relatório bruto)

1. **“contínua” vs. “absolutamente contínua”**: títulos [L772, L1549], [L1552, L1570, L1469, L1527, L2090] usam “contínua” como sinônimo, mas [L812–820] alerta que são noções distintas. Recomendação: reservar “absolutamente contínua” em definições/enunciados.
2. **Limites:** `$x\to\infty$` [L675, L748] vs. `$x\to+\infty$` [L527, L617] — escolher um.
3. **Capitulação:** `Distribuição Normal (Gaussiana)` [L1634] e `Seções 5.1--5.4 do Capítulo 5` [L297–298] destoa do resto em minúscula — padronizar.
4. **`de parâmetro` / `com parâmetro`**: [L739, L823] vs. [L1595, L1615, L1736, L1775] — unificar.
5. **`mais à frente` / `mais adiante`**: [L1646, L1873, L1902, L1426] — unificar.
6. **`isto é` / `ou seja`**, **`De fato` / `Com efeito`** ([L734]) — fixar padrão.
7. **Subscritos:** `$f_X$` vs. `$f_{X}$`, `$F_{X}'$` [L833–835] — uniformizar.
8. **Hífens:** `Borel mensuráveis` [L1440] vs. `Lebesgue-mensuráveis` [L862]; `bem definida` [L2270] vs. `bem-definida` [L2284]; `desvio padrão` [L1648] vs. `desvio-padrão` [L1675] — padronizar (`bem definida`, sem hífen, pelo Acordo).
9. **Delimitadores:** `\(…\)` nos exercícios [L2064–2091] vs. `$…$` no resto — unificar em `$…$`.
10. **Ênfase:** `\textbf{funções de distribuição}` [L429] isolado; resto usa `\emph` — trocar.
11. **`onde` locativo:** [L454] e [L1831–1832] — trocar por `em que` quando não for lugar.
12. **Sobrecarga de símbolos:** $\lambda$ = parâmetro exponencial/gama **e** medida de Lebesgue [L861–878]; considerar renomear a medida ($\ell$, $m$) ou alertar o leitor. Idem `\mathrm{N}` vs. `N` [L1638, L1650, L1664, L1691] e `dashed` descrito como `pontilhada` [L1695–1696] quando o correto é `tracejada`.
13. **Legendas:** só `fig:variavel-aleatoria` [L396] e `fig:construcao-cantor-medida` [L2198–2199] sem ponto final; a última ainda usa `\small\emph`, as demais não — uniformizar (ponto final, sem comando de fonte). `\caption` da `tab:densidades-usuais` [L1861] após o `tabular`; convenção ABNT/LaTeX pede acima da tabela.
14. **Espaços em fim de linha:** [L404, L795, L803, L817, L914, L1316, L1463] — limpar.
15. **Contradomínio da densidade:** `$f_X:\mathbb{R}\to[0,+\infty]$` [L795] vs. `$f:\mathbb{R}\to[0,\infty)$` [L1560] — unificar (admitir $+\infty$ ou não, explicitamente).

---

## B. Matemática (fonte: `agent-output/revisao-matematica.md`)

Legenda de severidade usada abaixo: **ERRO** = afirmação falsa; **GAP** = passo faltante; **IMPRECISÃO** = enunciado/demonstração imprecisa mas recuperável; **SUGESTÃO** = clareza/robustez, sem correção obrigatória.

### B1. Exige correção antes de publicar

- **[IMPRECISÃO — L1469–1478, L1527, L1540–1547]** `Se $X$ é contínua com densidade $f_X$` / `em uma variável aleatória contínua` / classificação “discreto vs. contínuo”. Pela \Cref{def:va-continua} [L791–804] e pela própria ressalva [L812–820], o correto é **“absolutamente contínua”**. Sem isso o teorema é falso na leitura ampla de “contínua” (a distribuição de Cantor é contínua, sem átomos, e não satisfaz \eqref{eq:prob-intervalo}). **Correção:** trocar por “absolutamente contínua” nos três lugares (+ [L1552, L1570, L2090]).
- **[GAP — L1438–1466 aplicado em L1481–1510]** TCD/\Cref{cor-TCD} enunciados para funções **Borel**-mensuráveis, mas a densidade da definição é só **Lebesgue**-mensurável. **Correção (escolher uma):** (i) enunciar TCD/corolário para Lebesgue-mensuráveis; ou (ii) fixar versão Borel da densidade. A aplicação em si é válida (`$\mathds{1}_{[x-1/n,x]}\to\mathds{1}_{\{x\}}$` pontualmente, dominação por $|f_X|\in L^1$ via normalização) — só o enquadramento de hipóteses está inconsistente. Aproveitar para invocar explicitamente a integrabilidade de $f_X$ na “última igualdade” [L1503].
- **[IMPRECISÃO — L2140–2154, exercise:densidade-arcoseno]** Enunciado dá $F(x)=c\arcsen\sqrt{x}$ só em $0<x<1$, sem $F=0$ ($x\le0$), $F=1$ ($x\ge1$) e sem fixar a constante aditiva. **Correção:** completar a definição por partes e obter $c=2/\pi$ (pois $\arcsen\sqrt{x}:0\to\pi/2$ e $F(0+)=0$).

### B2. Complementos de prova recomendados (não são erros, mas faltam para publicação)

- **[GAP — L973–988 + L2245–2291]** Convergência uniforme $f_n\to\mathcal{C}$ apenas afirmada e remetida aos exercícios. **Sugestão:** citar no corpo a estimativa de contração `$\|Tf-Tg\|_\infty\le\frac12\|f-g\|_\infty$` (provada no exercício) como justificativa, ou remissão explícita ao `starredexercise`.
- **[GAP — L2245–2291, em especial item (e)]** Para Banach: explicitar que $V$ é fechado em $C([0,1])$ (logo completo), que $T:V\to V$ (colagem usa $f(0)=0$, $f(1)=1$), e **provar que $T$ preserva monotonicidade** — sem isso o item (e) não conclui que $\mathcal{C}$ é não decrescente (o limite uniforme de monótonas é monótono, mas é preciso que cada $f_n$ seja monótona; $f_0(x)=x$ é, falta o passo indutivo).
- **[GAP menor — L791–804 + L895–910]** Definição admite densidade só Lebesgue-mensurável, mas o texto depois “deriva $F_X$ e toma a derivada como densidade” sem mencionar a versão mensurável. **Sugestão:** uma frase — “$F_X$ absolutamente contínua é derivável q.t.p.; a derivada, modificada num conjunto nulo pela regra \eqref{eq:densidade-derivada}, é (uma versão de) densidade”.

### B3. Cantor — verificado, com 3 lapidações opcionais

- [L1088–1093, L1152–1157] $X_n$ = extremo esquerdo, $I_n=[X_n,X_n+3^{-n}]$ — consistente. **Sugestão:** dizer “único **componente** de $K_n$” em vez de “único intervalo”, evitando confusão com extremos/representações ternárias.
- [L1203–1222] $P(X=x)\le2^{-n}$ — correto, **inclusive nos extremos** de intervalos removidos (cada $K_n$ tem um único componente contendo $x$; componentes fechados distintos não compartilham extremos). Só trocar “único intervalo restante” por “único componente” e justificar em uma linha.
- [L1263–1292] Recursão de $F_X$ nos 3 casos — correta, inclusive em $1/3$ e $2/3$ (contribuição de $Y=0$ tem prob. zero). Para blindar: reiterar que $Y\stackrel{d}=X$ e $Y\perp B_1$ no momento do condicionamento.
- [L1315–1339] Unicidade via $D\le D/2$ — completa ($D<\infty$ por continuidade em compacto; a equação impõe $G(0)=0$, $G(1)=1$). **Sugestão:** registrar essas duas frases; hoje as condições de contorno estão implícitas.
- [L1341–1344] Extensão $F_X=0$ ($x<0$), $F_X=1$ ($x\ge1$) — correta; acrescentar `$\mathcal{C}(1)=1$` para explicitar a colagem contínua em $1$.
- [L1349–1362] “Sem densidade” via $\int_{\mathbb{K}}f_X=0\ne1$ — correto ($\mathbb{K}$ fechado ⇒ mensurável; $f_X$ Lebesgue-mensurável por definição). Dizer “Lebesgue-mensurável”, não “Borel”.

### B4. Densidades usuais e beta–gama — corretas (nada a corrigir)

- Uniforme/exponencial/normal/Cauchy/gama/beta/qui-quadrado: normalizações, trocas ($x=\mu+\sigma\sqrt2\,z$, $y=\lambda x$, $x=\cos^2\theta$) e jacobiano $2r\sin\theta\cos\theta$ conferem. Tabela `tab:densidades-usuais` coerente com o texto. Observações: (i) explicitar $\Gamma(s+t)>0$ antes de dividir [L1985]; (ii) citar Tonelli também ao separar as integrais em $r$ e $\theta$ (sobretudo $s,t<1$) [L1957]; (iii) declarar que valores da densidade em pontos/extremos são irrelevantes (igualdade q.t.p.) para não sugerir unicidade pontual [L1593–1603, L1798–1801]; (iv) $B(1,1)=1$ ⇒ uniforme — ok.

### B5. Exercícios — verificados (1 correção + precisões)

- [exercise:fd-por-partes, L2082–2092] É de fato FD (limites $0$/$1$, monótona, contínua em $0$ com $F(0)=1/2$); densidade q.t.p.: $-x/(1+x^2)^2$ ($x<0$), $2x/(1+x^2)^2$ ($x>0$); valor em $0$ irrelevante. Sem erro.
- [exercise:soma-massas-intervalo, L2006–2014] Correto ($a,b$ inteiros, $F_X(b)-F_X(a)=P(a<X\le b)$); **sugestão:** escrever $\sum_{k=a+1}^{b}p_k$ em vez de notação pontilhada.
- [exercise:descontinuidade-ponto-massa, L2016–2020] Recíproca **é verdadeira** pela \Cref{rem:atomo-limite-esquerda} ($F_X$ descontínua em $c$ ⟺ $P(X=c)>0$).
- [exercise:existencia-mediana, L2028–2036] Sugestão $m=\inf\{t:F_X(t)\ge1/2\}$ funciona; solução deve exibir: conjunto não vazio (limite $+\infty$), limitado inferiormente (limite $-\infty$), $F_X(m)\ge1/2$ (cont. à direita), $P(X<m)\le1/2$ (limite à esquerda).
- [exercise:normalizacao-exponencial-modulo, L2050–2057] $c=1/2$ (para referência da solução).
- [exercise:densidade-valor-extremo, L2094–2101] Normalizada; $F(x)=\exp(-e^{-x})$, $F'=f$, limites $0$/$1$.
- [exercise:gama-exponencial, L2106–2111] “sse $w=1$” correto.
- [exercise:integral-gaussiana, L2126–2138] Correto; referência futura resolve com duas compilações (ver §C).
- [exercise:medida-cantor, L2156–2242] Correto ($R_n$ = $2^{n-1}$ abertos disjuntos, série soma $1$); explicitar que extremos removidos permanecem em $K_n$.

---

## C. LaTeX / referências cruzadas (sem erro bloqueante)

- `thm-TCD`/`cor-TCD` usam hífen em vez de `:` — funciona, mas inconsistente com o resto (`def:`, `eq:`, `fig:`, `exercise:`). Manter ou renomear globalmente, a seu critério.
- `eq:densidade-aprox` dentro de `align` com `\label` na última linha — correto.
- `exercise:integral-gaussiana` referenciado em [L1703, L1882] antes de definido em [L2126] — LaTeX resolve com duas compilações; sem referência quebrada no levantamento estático. Recomendação: recompilar duas vezes e conferir o `.log` por `undefined references`.
- `\,dx` e `q.t.p.` vs. `quase todo ponto` — padronizar (segunda forma preferível no texto introdutório).

---

## D. Prioridades sugeridas (para sua decisão)

| # | Ação | Linhas | Esforço |
|---|------|--------|---------|
| 1 | `raíz` → `raiz`; vírgulas sujeito–verbo [L973, L806, L841, L1369, L1646, L1458]; concordâncias [L813, L788] | A2 | 5 min |
| 2 | “contínua” → “absolutamente contínua” nos enunciados | L1469, L1527, L1540–47, L1552, L1570, L2090, L772 (título) | 5 min |
| 3 | TCD: trocar “Borel” por “Lebesgue” (ou fixar versão Borel da densidade) + invocar $\|f_X\|\in L^1$ | L1438–1466, L1503 | 10 min |
| 4 | Completar arco-seno ($F=0/1$ fora, $c=2/\pi$) | L2140–2154 | 5 min |
| 5 | Banach: $V$ fechado/completo, $T:V\to V$, $T$ preserva monotonicidade | L2245–2291 | 15 min |
| 6 | Uniformidade editorial (símbolos, hífens, capitulação, legendas, $\lambda$) | A4 | 20–30 min |
| 7 | Lapidações Cantor (“componente”, contornos $G(0),G(1)$, $\mathcal{C}(1)=1$) | B3 | 10 min |

---

## E. O que NÃO fazer (limites desta revisão)

- Não foi verificada compilação (`pdflatex`/`latexmk`), nem medição de overfull/underfull, nem conferência pixel a pixel das figuras TikZ (apenas coerência código–legenda, ex. `dashed` = tracejada).
- Não foi conferida a bibliografia (`GrimmettWelsh2014`, `MR2893652`) contra MathSciNet — fica como passo opcional.
- A matemática além do escopo do curso (teoria da medida geral) foi assumida como pano de fundo; os gaps apontados são os que afetam o argumento interno das notas.
