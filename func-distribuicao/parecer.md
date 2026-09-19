# Parecer consolidado — `func-distribuicao.tex`

**Arquivo revisado:** `/Users/cioletti/Documents/MProb/func-distribuicao/func-distribuicao.tex` (2489 linhas, 7 seções)
**Data:** 18/09/2026
**Método:** 10 subagentes independentes (`ds-flash`) lançados em paralelo, um por bloco
do arquivo, cada um gravando relatório próprio em `agent-output/revisao-blocoN.md`
(1: preâmbulo/abstract; 2: §1.1; 3: §1.2–1.3; 4: §2–3; 5: §4.1; 6: §4.2–4.6;
7: Cantor A; 8: Cantor B; 9: §5; 10: exercícios/bibliografia). **Auditoria:** reli os
10 relatórios, recompilei o documento (`latexmk -g -pdf`, exit 0, **0** Overfull/Underfull,
**0** referências indefinidas, **0** `LaTeX Warning`), conferi os rótulos órfãos por
`grep`, reproduzi o teste do `geometry` isoladamente e verifiquei as duas referências
no MathSciNet.
**Ação sobre o `.tex` e o `.bib`:** nenhuma. Este `parecer.md` é o único arquivo novo.

## Veredito global

A matemática do texto está **sólida**: os 10 revisores não encontraram um único erro
em teorema central — FD e propriedades, uniforme/exponencial, caracterização, densidades
usuais (todas as normalizações e a relação beta–gama), Cantor (cota $2^{-n}$ nos átomos,
recursão nos três terços, unicidade $D\le D/2$, ausência de densidade) e **todos** os
exercícios (inclusive `fd-por-partes`, arcoseno com $c=2/\pi$ e a construção via Banach).
O que resta são **um defeito gráfico inequívoco**, ~10 lacunas de justificação/remissão e
um conjunto de ajustes editoriais. Nenhum item bloqueia a leitura; a compilação é limpa.

A auditoria também **rejeitou quatro alertas** dos subagentes (layout do `geometry`,
`lucide-icons`, *option clash* do `babel` e previsão de `Overfull` na tabela) — ver §D.

---

## A. Erros confirmados (corrigir)

- **A1. Figura `fig:fd-discreta` (L470–509) fora de escala — `\Cref`→`✓ confirmado`.**
  Os patamares são desenhados em $0{,}40;\,1;\,1{,}3;\,1{,}8;\,2{,}3;\,3{,}6$ (L476–489)
  e o nível $3{,}6$ é rotulado como ``$1$'' (L503), com eixo até $5{,}18$ (L475). Como
  $F_X:\mathbb{R}\to[0,1]$, a figura sugere valores $>1$ e um salto final de massa
  $1{,}30$: os saltos somam $3{,}60$, não $1$. **Correção:** renormalizar (p.ex. massas
  $0{,}10/0{,}20/0{,}15/0{,}20/0{,}15/0{,}20$ ⇒ patamares $0{,}10/0{,}30/0{,}45/0{,}65/0{,}80/1{,}00$)
  e encurtar o eixo vertical para $\approx1{,}3$; manter a guia tracejada (L493) no nível
  final $1$. *(A chamada ``reta espúria'' do bloco 2 estava mal diagnosticada: a tracejada
  é uma guia legítima; o problema é só a escala.)*
- **A2. Notação de evento (L455) — `\Cref`→`✓ confirmado`.** ``o evento $X\leqslant x$
  ocorre'' deve ser ``o evento $\{X\leqslant x\}$ ocorre''; a notação sem chaves já fora
  fixada em L407–408.
- **A3. ``Lebesgue-Mensurável'' (L881, nota de rodapé) — `\Cref`→`✓ confirmado`.**
  Grafia correta: `Lebesgue-mensurável` (assim em L1111, L1124, L1126).
- **A4. Micro-erros de redação (blocos 5) — `✓ confirmado`.** L909 ``Nesta nota'' →
  ``Nestas notas''; L992 ``que como veremos é'' → ``que, como veremos, é'' (e remover
  espaço em fim de linha).

## B. Lacunas (GAPs) que merecem decisão

- **B1. Continuidade por cima/por baixo da probabilidade nunca enunciada — `✓ confirmado`.**
  Invocada em L571, L576 e L587; `grep` confirma que a expressão só aparece nesses três
  pontos. Como a nota se propõe autocontida, convém um lema/recordação antes de L568.
- **B2. `rem:atomo-limite-esquerda` (L678) sem prova — `✓ confirmado`.** Enuncia
  $F_X(x^-)=\lim_{\epsilon\downarrow0}F_X(x-\epsilon)$ e $\mathbb{P}(X=x)=F_X(x)-F_X(x^-)$,
  usados depois na seção de Cantor (L1558) e em exercício (L2187). Provar em 3 linhas via
  continuidade por baixo.
- **B3. TCD: hipóteses e prova do corolário — `✓ confirmado`.**
  (i) O TCD (L1122) e o corolário (L1140) falam em funções **Borel**-mensuráveis, mas a
  densidade da definição só é **Lebesgue**-mensurável; uniformizar (enunciar para
  Lebesgue-mensuráveis ou fixar versão Borel da densidade).
  (ii) L1127–1131 permite ler o conjunto excepcional como dependente de $n$; fixar um único
  $N$ com $\lambda(N)=0$.
  (iii) O corolário não é provado nem ligado ao TCD, e `thm:convergencia-dominada` (L1123)
  é **rótulo órfão** (`grep`: só a própria definição). Inserir a prova de 3 linhas via
  $f_n=f\mathds{1}_{I_n}$ e citar o teorema.
- **B4. Passo $\int_{\{x\}}f_X=0$ não explicitado (L1187–1189) — `✓ confirmado`.**
  O corolário dá a convergência; falta dizer que $\lambda(\{x\})=0$ e $f_X\in L^1$
  implicam a última igualdade.
- **B5. Critério de densidades (L1084–1107) em prosa — `✓ confirmado`.** Não é ambiente
  numerado; a justificativa ``limites em $\pm\infty$ seguem da continuidade da integral''
  (L1102) é vaga e usa limite sob integral só provado na subseção seguinte. Recomenda-se
  `proposition`/`proof` e remissão explícita.
- **B6. Derivada q.t.p. como densidade (L998–1009) — `✓ confirmado`.** Resultado central
  em prosa, sem label nem citação (``que usaremos sem demonstrar'').
  Sugestão: `theorem` com `\label` e `\cite{MR2893652}`.
- **B7. Rótulos órfãos — `✓ confirmado` por `grep`.** `rem:densidade-qtp` (L1028) e
  `rem:medida-lebesgue-qtp` (L955) nunca são `\Cref`-ados; `eq:densidade-aprox` (L1064)
  e `eq:conjunto-cantor`/`eq:funcao-distribuicao-cantor` também não. Usar ou remover.
- **B8. Observação ``contínua vs. absolutamente contínua'' (L1016–1024) não remete a
  Cantor — `✓ confirmado`.** É o lugar natural para `\Cref{sec:distribuicoes-singulares}`.
- **B9. Cantor: ordem lógica e remissões — `✓ confirmado`.**
  - $T$ é usado em L1264 antes de ser definido (só o exercício L2433 o define);
  - $X$ é usado em L1496–1497 antes de (2) em L1505 (a cota de Cauchy pressupõe a
    convergência que quer provar); definir $X$ como limite das somas parciais primeiro;
  - a convergência uniforme (L1302–1312, L1641) é apenas afirmada: exibir a contração
    $\|Tf-Tg\|_\infty\le\tfrac12\|f-g\|_\infty$ e remeter a
    `\Cref{exercise:construcao-cantor-avancada}`;
  - L1311 fala em ``lista de exercícios avançados'' (inexistente);
  - falta $\mathcal{C}(0)=0$ para justificar a extensão por $0$ (L1677); e falta remissão a
    `exercise:medida-cantor` no uso de $\lambda(\mathbb{K})=0$ (L1319, L1686).
- **B10. Banach não enunciado — `✓ confirmado` (bloco 10).** O item (c) do
  `starredexercise` (L2463–2465) manda usar o Teorema do Ponto Fixo de Banach, que não é
  enunciado nem referenciado em parte alguma. Uma linha ou `\cite`. No item (e)
  (L2472–2478), a continuidade já foi obtida em (c); pedir só a monotonicidade.

## C. Matemática verificada (sem erro)

- **FD e propriedades (§1–3), bloco 3/4:** proposição (i)–(iii), definição de átomo, lei
  $\mu_X$, $\mathbb{P}(a<X\le b)=F_X(b)-F_X(a)$, uniforme e exponencial (extremos e
  continuidade) e o teorema de caracterização (necessário e suficiente) conferem.
- **Densidades (§5), bloco 9:** normalizações uniforme/exponencial/normal (mudança
  $x=\mu+\sigma\sqrt2\,z$)/Cauchy/gama ($y=\lambda x$)/beta/qui-quadrado, domínios, a
  identificação $\chi_n^2=\text{gama}(n/2,1/2)$ e a prova beta–gama (jacobiano
  $2r\operatorname{sen}\theta\cos\theta$, Tonelli, $x=\cos^2\theta$) estão corretas.
- **Cantor (§5), blocos 7/8:** $K_n$, recursão $T$, expansão ternária, $\mathbb{P}(X=x)\le2^{-n}$
  (inclusive nos extremos $1/3$, $2/3$), recursão de $F_X$, unicidade sem usar
  monotonicidade, extensão $0/1$ e inexistência de densidade conferem.
- **Exercícios, bloco 10:** os 17 itens conferem. Destaque de gabarito: em
  `exercise:fd-por-partes` a densidade é $f(x)=\dfrac{|x|}{(1+x^2)^2}$, **não**
  $2x/(1+x^2)^2$ para $x>0$.
- **Densidades anteriores:** a nota já incorporou correções de pareceres prévios (o
  exercício do arco-seno já traz as três partes e $c=2/\pi$; o exercício de medida de
  probabilidade já foi movido para a lista final; Cantor já é seção própria).

## D. Achados rejeitados ou atenuados pela auditoria

- **✗ `geometry` anula os `\setlength` (bloco 1).** **Rejeitado.** Teste reproduzido:
  com `\usepackage{geometry}` + `\setlength{\textheight}{9.55in}`, o valor final é
  $690{,}18$pt ($\approx9{,}59$in); só `geometry`, sem os `\setlength`, dá $556{,}48$pt.
  Os ajustes manuais **vigoram**.
- **✗ `lucide-icons` pode inviabilizar o pdflatex (bloco 1).** **Atenuado.**
  `latexmk` retorna exit 0 sem avisos. O pacote **não é usado** em lugar algum; remover é
  limpeza, não correção.
- **✗ *option clash* `portuguese`/`brazilian` (bloco 1).** **Rejeitado.** Compilação limpa,
  sem *option clash*.
- **✗ `Overfull \hbox` na tabela (bloco 9).** **Não observado.** O log não registra
  Overfull/Underfull.
- **~ ``derivabilidade de $F_X$ $\Rightarrow$ densidade'' é ERRO (bloco 6, L1078–1080).**
  **Atenuado.** O sujeito da frase é ``uma variável aleatória **absolutamente contínua**
  $X$''; não se afirma que derivabilidade isolada baste. Resta imprecisão: citar
  `\eqref{eq:densidade-derivada}` e dizer ``derivável em quase todo ponto''.
- **~ ``reta tracejada espúria'' (bloco 2, L493).** **Reinterpretado:** é guia de nível;
  o defeito real é a escala (A1).

## E. Consistência editorial (polimento)

1. **Delimitadores:** exercícios usam `\(...\)` (L2236, 2241, 2245, 2251) — uniformizar em `$...$`.
2. **Legendas:** `fig:construcao-cantor-medida` (L2373) usa `\small\emph{...}`; as demais não usam comando de fonte — padronizar (e ponto final).
3. **`\break` frágeis** (L1877, L1951, L2016, L2148): em modo horizontal quebram linha, não página; trocar por `\clearpage` se a intenção é nova página.
4. **TikZ duplicado:** o diagrama de `fig:construcao-cantor-distribuicao` (L1349–1382) é idêntico ao do exercício (L2343–2376); extrair um macro (como já se fez com `\CantorApproximation`).
5. **Seção 5 lista a Cauchy sem parâmetros (L1862)** enquanto L1725 diz ``cada uma acompanhada de seus parâmetros''; a normalização da Cauchy aparece duas vezes (L1867–1873 e L2036–2046) — remeter.
6. **Ponto de medida de Lebesgue duplicado:** $(\mathbb{R},\mathscr{B}(\mathbb{R}),\lambda)$ e $\lambda((a,b])=b-a$ em L624–631 e de novo em `rem:medida-lebesgue-qtp` (L954–962); a primeira menção é prematura (achado ainda válido do parecer de estrutura).
7. **Valores nos extremos:** uma frase na abertura da §5 (``valores em finitos pontos não alteram a integral'') cobre uniforme/gama/beta/qui-quadrado.
8. **Colisão de notação** em L2116: $x=\cos^2\theta$ reusa $x$ do integrando; usar outra letra.
9. **Uniformidades menores:** `$f_X$` vs `$f_{X}$`; `onde` locativo → `em que`; `\sin`→`\sen` (macro já faz); espaços em fim de linha (L404, L670, L985, L992, L1316, L1463); rótulos `thm-TCD`/`cor-TCD` fogem da convenção `prefixo:`.

## F. Referências (MathSciNet)

Verificadas com `mathscinet` (uma por vez, `sleep 10`):
- **`MR2893652`** (Billingsley, *Probability and measure*, anniversary ed., 2012) — **confere** com a entrada canônica.
- **`GrimmettWelsh2014`** = **MR3243603** (Grimmett–Welsh, *Probability—an introduction*, 2nd ed., 2014) — **confere**; o `.bib` já traz `MRNUMBER = 3243603` e `MRREVIEWER`.
  Ambas **verificadas**.

## G. Prioridades sugeridas

| # | Ação | Linhas | Esforço |
|---|------|--------|---------|
| 1 | Renormalizar `fig:fd-discreta` (A1) | 470–509 | 15 min |
| 2 | Notação `\{X\le x\}` e micro-ortografia (A2–A4) | 455, 881, 909, 992 | 5 min |
| 3 | Provar `rem:atomo-limite-esquerda` e enunciar continuidade da probabilidade (B1–B2) | 678, 568 | 10 min |
| 4 | TCD: mensurabilidade, conjunto nulo único, prova do corolário (B3–B4) | 1122–1195 | 15 min |
| 5 | Numerar critério, teorema da derivada e remissões faltantes (B5–B8) | 998–1107, 1016 | 15 min |
| 6 | Cantor: definir $T$/$X$ antes, citar o exercício, $\mathcal C(0)=0$ (B9) | 1264, 1309, 1496, 1677 | 15 min |
| 7 | Banach e encadeamento do item (e) (B10) | 2463–2478 | 5 min |
| 8 | Polimento editorial (§E) | vários | 20–30 min |

## H. Limites desta revisão

- Revisão por blocos independentes: as fronteiras (p.ex. L701–712, L1016 ou L1490) foram
  reexaminadas por mim na auditoria para não perder achados de costura.
- Não houve conferência visual pixel a pixel das figuras TikZ, nem revisão de estilo
  tipográfico da editora; o foco foi correção, rigor, coerência e referências.
- Relatórios brutos dos 10 blocos em `agent-output/revisao-bloco1.md` … `revisao-bloco10.md`.
