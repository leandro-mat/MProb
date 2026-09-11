# Estilo e voz das notas MProb

Guia consolidado de escrita, extraído dos oito digests de estilo e de
`NOTACOES-E-CONVENCOES.md`. Destina-se a quem redige ou reescreve uma nota (no
momento: a nota de funções geradoras). Reúne os **padrões comuns** às notas já
existentes, com exemplos curtos e referências `nota.tex:linha`. Abreviações de
arquivo usadas abaixo:

- `prop-prob.tex` = `prop-prob/prop-prob.tex`
- `indep.tex` = `independencia/independencia.tex`
- `va.tex` = `variaveis-aleatorias/variaveis-aleatorias.tex`
- `esp.tex` = `esperanca-discreta/esperanca-discreta.tex`
- `esp-cond.tex` = `esp-condicional/esp-condicional.tex`
- `vet.tex` = `vetores-discretos/vetores-discretos.tex`
- `ind-va.tex` = `ind-va-discretas/ind-va-discretas.tex`
- `sup-inf.tex` = `sup-inf/capitulos/capitulo1.tex` / `capitulo2.tex`

---

## 1. Voz, pessoa e tom

- **Primeira pessoa do plural inclusiva** ("nós = autor + leitor"), nunca "eu".
  `vamos mostrar`, `obtemos`, `concluímos`, `observamos` (prop-prob.tex:307;
  indep.tex:435; esp-cond.tex:427).
- **Imperativos didáticos de condução**: `Considere`, `Seja`, `Suponha`,
  `Fixe`, `Defina`, `Tome` (esp.tex:235; ind-va.tex:299; prop-prob.tex:464).
- **Perguntas retóricas** abrem motivações e seções (prop-prob.tex:505
  "Por que exigir o fechamento sob uniões enumeráveis?"; indep.tex:481;
  ind-va.tex:714-722).
- **Sobriedade**: tom professoral, expositivo, sem floreio. Importância é
  mostrada pela matemática, não por adjetivos.
- **Metacomentário didático** é permitido e recorrente: o autor comenta o
  próprio percurso ("Acreditamos que esses detalhes são instrutivos",
  va.tex:958-962; "Vale registrar que...", vet.tex:704,2884).
- Primeira pessoa possessiva: "em nosso espaço", "nossa análise"
  (indep.tex:278,503).

## 2. Frases e conectivos padrão

| Expressão | Quando usar | Exemplo |
|---|---|---|
| `Vamos ...` | anunciar etapa/cálculo | "Vamos dividir a demonstração em três etapas." (vet.tex:758) |
| `Note que` / `Observe que` | chamar atenção para fato lateral | "Note que $\operatorname{Im}X$ é enumerável." (va.tex:327) |
| `De fato` / `Com efeito` | justificar afirmação imediatamente anterior | "De fato, pelo teorema binomial." (va.tex:604) |
| `Isto é` / `ou seja` | reformular/parafrasear | "isto é, $A_i\cap A_j=\varnothing$." (indep.tex:355) |
| `Como ..., segue que ...` | encadear dedução | "Como $\mathbb{R}=\mathbb{Q}\cup\mathbb{I}$, segue que..." (sup-inf.tex) |
| `Portanto` / `Logo` / `Assim` | fechar dedução | "Assim, $p_X(x)$ é a probabilidade de..." (va.tex:326) |
| `Por outro lado` / `No entanto` | contrapor | "Por outro lado, se a sequência é monótona..." (sup-inf.tex) |
| `Analogamente` / `de modo análogo` | dispensar passo simétrico | "o cálculo para $p_Y$ é análogo" (ind-va.tex:436) |
| `Resta ...` | signposting de etapa final | "Resta identificar o valor dessa série." (esp-cond.tex:522) |
| `Recorde que` / `convém recordar` | retomar fato anterior | "Recordemos a identidade..." (esp-cond.tex:733) |
| `Antes de ...` | preparar verificação | "Antes de aplicar o Teorema, vamos verificar a hipótese." (esp-cond.tex:755) |
| `Primeiro ... / Em seguida ... / Finalmente ...` | ordenar passos | "Vamos analisar o limite de cada fator. Primeiro, ..." (va.tex:1061) |
| `Suponha que` / `Seja` | instaurar hipótese | "Seja $X$ uma variável aleatória discreta." (esp.tex:235) |

Fórmulas de remate de raciocínio: `o que encerra a demonstração`,
`Isso conclui a prova`, `como desejado`, `o que prova a afirmação`
(esp.tex:341,665; va.tex:1084).

## 3. Ritmo expositivo

- **Abertura de seção** retoma a nota anterior ou anuncia o problema, em tom
  ensaístico, antes de qualquer formalismo (ind-va.tex:238-245; prop-prob.tex:683;
  indep.tex:617).
- **Fechamento de seção** costuma apontar o próximo passo ou amarrar ao que foi
  anunciado na abertura, não resumir "nesta seção vimos" (vet.tex:2925-2932;
  va.tex:485-486; esp-cond.tex:607).
- **Transições de bloco** explícitas: "Apresentamos agora...", "É hora de...",
  "Reunimos as ideias discutidas nas seções anteriores na próxima definição."
  (prop-prob.tex:813; sup-inf.tex:184).
- **Fecho de prova**: sempre com `\qedsymbol=\blacksquare`; frequentemente
  acompanhado de frase verbal ("o que encerra a demonstração").
- **`\bigskip`/`\medskip`** separam blocos conceituais (nunca meramente
  decorativos). `\bigskip` isola perguntas, exemplos e mudanças de assunto
  (vet.tex:368,455,1654; va.tex:272,568). Para divisões internas de prova usa-se
  ```tex
  \medskip
  \noindent\textbf{Parte 1.}
  ```
  (vet.tex:765; indep.tex:1110). `\noindent\textbf{...}` também marca
  mini-seções dentro de exemplos longos e cabeçalhos de distribuições
  (prop-prob.tex:1606; va.tex:570).

## 4. Equações

- **Display dominante**: `\[ ... \]` sem numeração para álgebra de passagem.
  Nunca `$$...$$`.
- **Numeração seletiva**: numera (`equation`/`align`) só o que será citado
  depois por `\eqref` (definições-chave, enunciados, identidades reutilizadas).
  Linhas intermediárias levam `\notag`/`\nonumber` (va.tex:990-1007;
  ind-va.tex:735).
- **Alinhamento**: `align*`/`aligned` com `&=` na primeira relação, uma etapa
  por linha; cadeias longas quebram em linhas físicas (vet.tex:1232-1257).
  `alignedat` quando há várias colunas coordenadas (prop-prob.tex:976).
- **Espaçamento vertical**: escolhido pela densidade visual, não automático.
  `\\[0.3cm]` é o padrão usual; `\\[0.4cm]` para `\substack`/delimitadores
  altos; `\\[0.2cm]` para separação leve; `\\[0.6cm]` para linhas densas
  (esp.tex:733,739; vet.tex:586). Não espalhar por hábito.
- **Pontuação terminal**: a fórmula faz parte da frase. Vírgula na penúltima
  linha, ponto na última quando a frase fecha (`= 1.`, va.tex:347;
  `= e^{-\lambda}\frac{\lambda^k}{k!},`, va.tex:1082).
- **`\text{...}`** reservado a qualificadores curtos (`\text{se }`,
  `\text{para }`, `\text{caso contrário,}`) e conectores (`\text{ e }`,
  `\qquad\text{enquanto}\qquad`). **Justificativas de passagem vão em prosa, fora
  do display**: "onde a separação da soma dupla em um produto é autorizada pela
  convergência absoluta..." (ind-va.tex:347-348; esp.tex:863-864).
- Separação horizontal com `\quad`/`\qquad`; `\,` antes de probabilidades
  (vet.tex:263; esp.tex:448).
- Convenções: `\operatorname{Im}X`; `\mathbb{P}`, `\mathbb{E}`; `\mathds{1}_A`;
  `\leqslant/\geqslant`; `\mid`/`\bigm|` para condicional; vírgula decimal
  `0{,}3`; `\equiv` para identificações notacionais (ver `NOTACOES-E-CONVENCOES.md` §6).

## 5. Provas

- **Abertura** sem preâmbulo genérico: entra direto no argumento ou anuncia a
  estratégia. Padrões: hipótese ("Seja $B\in\mathcal{F}$ com
  $\mathbb{P}(B)>0$", esp-cond.tex:363); construção ("Seja $S_N$ o conjunto...",
  prop-prob.tex:1326); estratégia ("Provaremos por contradição...",
  sup-inf.tex:690); roteiro ("A prova tem duas etapas. Primeiro...",
  esp-cond.tex:427).
- **Signposting forte**, quase parágrafo a parágrafo em provas longas:
  "Primeiro vamos controlar...", "Para simplificar a notação, vamos definir...",
  "Próximo passo é...", "Resta...", `\bigskip` marcando as metades
  (esp-cond.tex:427-522; vet.tex:758-765).
- **Verificação de hipóteses**: antes de aplicar um teorema, checa-se
  positividade, convergência absoluta, mensurabilidade — em bloco separado e
  explícito ("Antes de aplicar o Teorema da Partição, vamos verificar a hipótese
  de somabilidade absoluta", esp-cond.tex:755).
- **Nível de detalhe**: álgebra conceitual (trocas de soma/limite, reindexação,
  decomposição disjunta) é **explicitada linha a linha** com justificativa
  (vet.tex:1603-1606; ind-va.tex:311-327). Álgebra mecânica de frações/fatoriais
  fica implícita (vet.tex:2274,2708).
- **Delegação explícita**: passos simétricos e induções são despachados por
  "análogo", "o mesmo argumento vale", ou remetidos a exercícios — sempre
  nomeando o que fica de fora (indep.tex:388; sup-inf.tex:1011).
- Provas de "se e somente se" marcam direções com `\noindent($\Longrightarrow$)`
  / `($\Longleftarrow$)` (ind-va.tex:299-305).

## 6. Definições e motivação

- **Padrão-mestre**: `intuição/exemplo concreto → narrativa → verificação →
  definição → ressalva sobre alcance` (esp-cond.tex:236-289; vet.tex:236-240;
  prop-prob.tex:453-484).
- **Exemplo-motivador antes da definição**: dado/urna/moeda concreto produz um
  número e então formaliza-se (esp.tex:429-436; va.tex:239-260).
- **Narrativa de descoberta e "por que esta construção"**: justifica escolhas
  axiomáticas e de notação (por que convergência absoluta, esp.tex:460-463;
  por que $J=g(D)$ e não $\operatorname{Im}Z$, vet.tex:1057-1067).
- **Tentativas que falham**: mostra a intuição errada antes de corrigi-la
  ("Essa intuição falha porque...", indep.tex:430; "O Exemplo X mostrou que não
  existe... Isso não significa que seja impossível...", prop-prob.tex:1147).
- **Heurística primeiro, rigor depois**: o cálculo heurístico antecede o
  enunciado preciso ("O cálculo heurístico ... pode ser transformado em um
  resultado preciso", va.tex:1025-1027).
- **Ressalvas didáticas pós-definição**: antecipar mal-entendido comum
  (vet.tex:1707-1711) e limites da teoria ("por enquanto só definimos...",
  esp-cond.tex:313).
- **Remissões a notas anteriores**: textuais, sem `\cite` ("Nas notas sobre
  vetores aleatórios discretos...", ind-va.tex:238; "Recorde das notas
  anteriores que...", esp-cond.tex:1154).
- Termo definido em `\emph{...}` na primeira aparição (va.tex:260,317;
  ind-va.tex:260).

## 7. Exemplos, observações e exercícios

- **Exemplos**: título entre colchetes, descritivo e temático; introduzidos por
  contexto e resolvidos por completo; terminam com uma moral/ponte teórica
  (sup-inf.tex:638; prop-prob.tex:1035). Encadeiam-se por `\Cref` a exemplos
  anteriores (va.tex:1124,1154).
- Exemplos conceituais são longos e detalhados; contraexemplos são exemplos de
  pleno direito ("A recíproca ... é falsa. O exemplo a seguir exibe...",
  ind-va.tex:505-510).
- **Observações**: `remark` usado como *post-scriptum* interpretativo logo após
  um resultado; também em prosa marcada por "Observe que" quando curtas. Muitas
  notas têm `remark` abundante como veículo de discussão (esp-cond.tex 8×;
  indep.tex 8×).
- **Exercícios**: agrupados ao fim de seção/bloco, introduzidos por frase de
  contexto ("Nos exercícios a seguir, $(\Omega,\mathcal{F},\mathbb{P})$ é um
  espaço de probabilidade.", prop-prob.tex:956). Enunciados imperativos
  (`Mostre que`, `Determine`, `Dê um exemplo`). **Sem gabarito**; `\emph{Sugestão:}`
  (ou `\emph{Dica:}`) fornece o mecanismo, não o resultado (esp-cond.tex:1008;
  va.tex:528). Exercícios carregam teoria e completam provas (sup-inf.tex:1352).
- Itens numerados com `enumerate` `(\alph*)`/`(\roman*)` (indep.tex; va.tex).

## 8. Figuras e tabelas

- **TikZ puro** é o padrão; PGFPlots (`axis`) só para gráficos de função
  (prop-prob.tex:1227; va.tex:612). Estilos locais por figura, nomes em
  português (`ponto`, `fibra`, `blob`); paleta sóbria: preto/cinza + `teal`
  para destaques (vet.tex:272,1101).
- **Legendas** descritivas, autossuficientes, em minúscula, com matemática e às
  vezes com valores concretos; podem conter `\Cref` interno (vet.tex:1186-1190;
  prop-prob.tex:1258).
- **Posicionamento**: `[H]` quando a proximidade é pedagógica, senão `[htbp]`.
  Figuras anunciadas em prosa antes de aparecer ("A Figura ilustra...",
  indep.tex:809).
- **Tabelas**: `booktabs` (`\toprule`/`\midrule`/`\bottomrule`), `\arraystretch`
  e `\tabcolsep` ajustados caso a caso, `\\[0.3cm]` entre linhas altas
  (vet.tex:379-389; va.tex:871-889). Nem toda nota usa tabelas — usar só quando
  ajuda.
- Figuras meramente ilustrativas sem legenda ficam em `center` sem `figure`
  (vet.tex:781).

## 9. Referências

- **`\Cref{...}`** (sempre maiúsculo, salvo início de frase minúsculo) para
  ambientes nomeados; **`\eqref{...}`** para equações. Nada de `\ref` cru para
  teoremas/equações (vet.tex:36 `\Cref`; ind-va.tex:16 `\eqref`).
- **Remissão entre notas é textual, sem `\cite`**: "nas notas sobre...",
  "como visto anteriormente", "em nota futura" (ind-va.tex:238,778;
  vet.tex:451,2889). Arquivos compilam separadamente — não há
  `\externaldocument`.
- **`\cite`** é raro e de "apoio", não de autoridade: fonte-base declarada no
  resumo ("O texto segue de perto as Seções 2.1-2.3 ... de Grimmett e Welsh
  \cite{GrimmettWelsh2014}", va.tex:206-207) e citações pontuais "veja
  \cite{...}" para o leitor aprofundar (vet.tex:651,702).
- `\label` logo após `\begin{...}`; em figuras/tabelas após `\caption`
  (NOTACOES §7). Prefixos padronizados (`thm:`, `def:`, `eq:`, `exercise:` etc.).

## 10. Nível de detalhe típico

**Explicita-se sempre**: reindexação e troca de somatório/limite com a hipótese
que autoriza (convergência absoluta, $\sigma$-aditividade); decomposição de
conjuntos; verificação de mensurabilidade/positividade antes de usar; contagens
combinatórias "de primeira mão"; interpretação qualitativa de cada resultado em
`remark` ou parágrafo final; casos patológicos (não omitidos).

**Delega-se ao leitor**, sempre nomeando o motivo: álgebra mecânica de
frações/fatoriais; passos simétricos ("análogo"); induções curtas; resultados
técnicos fora de escopo ("não a demonstraremos aqui", prop-prob.tex:1680);
generalizações e variações via exercícios. Onde algo é admitido, declara-se
("admita que a esperança de $W$ está bem definida", esp-cond.tex:1073).

**Calibragem**: nota de aula expositiva para graduação, "rigorosa e motivada",
mais explícita que livro-texto, privilegiando *entender por que* antes de
*enunciar o que*.

## 11. Coisas a evitar

- **`$$...$$`**: nunca; usar `\[...\]` (ocorre indevidamente em sup-inf.tex:474;
  ind-va.tex:647,747 — limpar).
- **Misturar `\mathscr{F}` e `\mathcal{F}`**: fixar `\mathcal{F}` para a
  $\sigma$-álgebra (ind-va.tex oscila entre 251 e 521). `\mathscr{P}` só para
  partes.
- **Travessões `---` na prosa**: substituir por vírgulas/parênteses/dois-pontos
  (NOTACOES §2). Hífens normais em compostos seguem permitidos.
- **Adjetivos enfáticos** sem conteúdo: `crucial`, `fundamental`, `poderoso`,
  `canônico`, `límpido`, `fantasticamente importante` (indep.tex:255,330;
  sup-inf.tex:319).
- **Numeração manual `\tag{}` e números de livro rígidos** em labels/argumentos
  opcionais (sup-inf.tex usa `\tag`; prop-prob.tex:717 — não reproduzir em
  conteúdo novo).
- **Typos e artefatos observados**: `sequência!limitada` com `!` vazando;
  "anuncio" sem acento; "um situação"; duplo espaço; acento em "exercicio"
  (sup-inf.tex:804,867; indep.tex:482,511; prop-prob.tex:1379).
- **Calcos de tradução** como "o verdadeiro negócio", "para estragar a surpresa"
  (sup-inf.tex) — preferir formulação portuguesa natural.
- **`\cref` minúsculo vs `\Cref`**: manter `\Cref` como padrão dominante.
- **Inconsistência de label**: escolher `eq:` (não `eq-aux1` solto) e manter o
  prefixo em toda a nota.

## 12. Checklist prático (nova seção / revisão)

1. Abertura retoma a nota anterior ou anuncia o problema em prosa, antes do
   formalismo?
2. Toda definição vem depois de intuição/exemplo concreto (e não o contrário)?
3. Escolhas não evidentes (notação, hipóteses, construção auxiliar) foram
   motivadas ("por que esta construção")?
4. Hipóteses (positividade, convergência absoluta, mensurabilidade,
   independência) verificadas antes de aplicar cada teorema?
5. Prova com signposting ("Primeiro...", "Resta...", "Passo 1/2/3") e
   `\noindent\textbf{Parte N.}` onde couber?
6. Álgebra conceitual (trocas de soma/limite, reindexação) explicitada linha a
   linha; álgebra mecânica deixada ao leitor com "análogo"/"o mesmo argumento"?
7. Só numera o que será citado; `\notag` nas linhas intermediárias; `\label`
   descritivo logo após `\begin{...}`?
8. Pontuação terminal correta nos displays (vírgula/ponto dentro do ambiente)?
9. Justificativas longas em prosa fora do display; `\text{...}` só para
   qualificadores curtos?
10. Espaçamento `\\[0.xcm]` escolhido pela densidade visual (0.3 cm padrão),
    não aplicado por hábito?
11. `\Cref` para ambientes, `\eqref` para equações, remissão textual (sem
    `\cite`) para outras notas?
12. Sem `$$...$$`, sem travessão em prosa, sem adjetivo enfático vazio?
13. Notação conforme `NOTACOES-E-CONVENCOES.md` §6 (`\operatorname{Im}X`,
    `\mathds{1}`, `\mid`, `0{,}3`, `\leqslant`, `X\overset{d}{=}Y`)?
14. Fechamento de seção amarra à abertura ou aponta o próximo passo?
15. Compilou (`latexmk -pdf -interaction=nonstopmode -halt-on-error`) e
    conferiu referências indefinidas / caixas excedentes?
