# Parecer de estrutura — `func-distribuicao.tex`

**Arquivo revisado:** `/Users/cioletti/Documents/MProb/func-distribuicao/func-distribuicao.tex` (2429 linhas)
**Data:** 18/09/2026
**Escopo:** estrutura e organização do texto — árvore de seções/subseções, cadeia de
dependências, colocação de objetos, coesão, duplicações, balanço e integração de
figuras/exercícios. Ortografia e correção matemática **não** são objeto deste
parecer (já cobertos por `parecer.md` e pelos relatórios em `agent-output/`).
**Compilação:** `latexmk -g -pdf` concluiu sem erros; `.log` com **0** referências
indefinidas, **0** `Overfull`/`Underfull` e **0** `LaTeX Warning`.
**Método:** mapa estrutural automático (labels e referências), duas passagens
independentes por subagentes — `ds-flash` (microestrutura) e `luna`
(macroestrutura/dependências) — e verificação direta dos achados mais
consequentes. Relatórios brutos em
`agent-output/revisao-estrutura-micro.md` (167 linhas) e
`agent-output/revisao-estrutura-macro.md` (253 linhas).
**Ação sobre o `.tex`:** nenhuma. Este parecer é o único arquivo novo.

---

## Veredito global

A arquitetura de fundo é boa e bem graduada: parte da experiência com variáveis
discretas, define função de distribuição e suas propriedades, exibe dois
exemplos, só então apresenta o teorema de caracterização e, em seguida, as
variáveis absolutamente contínuas e o catálogo de densidades. As dependências
lógicas válidas estão todas no lugar (não há uso de resultado antes de
enunciado), a compilação é limpa e as referências cruzadas resolvem.

Os problemas são de **enquadramento, proporção e colocação**, não de ordem
lógica. Há três pontos que valem correção: (i) o exercício embutido no corpo da
seção 1, que ainda por cima desloca a numeração da lista final; (ii) a seção 4,
cujo título ("absolutamente contínuas") exclui dois de seus conteúdos centrais
(o exemplo singular de Cantor e o TCD); (iii) a medida de Lebesgue, introduzida
e caracterizada duas vezes, a primeira prematura. O restante é ajuste de
proporção e de nomenclatura.

---

## Árvore atual

| Nº | Seção | Linhas | Subseções |
|----|-------|--------|-----------|
| 1 | Funções de Distribuição | 318–701 | 3 (Definição e exemplo discreto; Propriedades fundamentais; Átomos e probabilidades em intervalos) |
| 2 | Exemplos de Funções de Distribuição | 703–794 | — |
| 3 | Caracterização das Funções de Distribuição | 796–843 | — |
| 4 | Variáveis Aleatórias Absolutamente Contínuas | 844–1651 | 7 (Densidades…; Medida de Lebesgue…; Consequências…; TCD; Probabilidades de pontos e intervalos; Cantor; Recapitulação) |
| 5 | Algumas Funções de Densidade Usuais | 1653–2107 | 6 (Critério; Densidades básicas; Normal e Cauchy; gama/beta/qui-quadrado; Observações sobre normalização; relação beta–gama) |
| 6 | Exercícios propostos | 2109–2424 | — |

---

## Achados consolidados

Legenda: **GRAVE** = compromete a leitura/organização; **MÉDIO** = desalinha
título, conteúdo ou fluxo; **MENOR** = uniformidade e polimento.

### GRAVE

**G1. Exercício embutido no corpo da subseção 1.3, com cabeçalho duplicado e
numeração deslocada.** — linhas 649–655.
O único exercício do corpo está no meio da subseção 1.3, entre a definição da
lei $\mu_X$ e a discussão de átomo da lei. Como o ambiente já imprime
"Exercício N.", o `\textbf{Exercício.}` interno produz "Exercício 1. Exercício.".
Além disso, esse exercício consome o número 1: no `.aux`, o primeiro exercício
da lista final é `exercise:soma-massas-intervalo`, numerado **2**. O leitor,
portanto, não encontra o "Exercício 1" onde a lista começa.
*Sugestão:* mover o bloco para a seção 6 (sob um cabeçalho próprio, p.ex.
"Medidas e leis"), apagar o `\textbf{Exercício.}` e deixar no corpo uma frase de
transição ("a verificação de que $\mu_X$ é medida de probabilidade fica para a
lista de exercícios").

**G2. A seção 4 tem título que exclui parte do próprio conteúdo.** — linhas
844–1651, em especial 1179–1640.
A seção "Variáveis Aleatórias Absolutamente Contínuas" abriga (a) o exemplo de
Cantor, que é uma distribuição **contínua mas não absolutamente contínua**, e
(b) o Teorema da Convergência Dominada, ferramenta de teoria da medida. O
título faz o leitor esperar apenas densidades e o caso absolutamente contínuo, e
a subseção mais longa do texto (≈460 linhas) é justamente a que contradiz o
título. Isso também dificulta situar Cantor no plano anunciado no resumo.
*Sugestão (preferida):* separar em duas seções — manter 4 como "Variáveis
Aleatórias Absolutamente Contínuas" (definição, Lebesgue, propriedades, TCD,
probabilidades) e criar uma seção "Distribuições Contínuas sem Densidade: o
Exemplo de Cantor" a partir da linha 1179. Como a numeração é automática, o
custo é praticamente o de inserir um `\section`. Alternativa mínima: renomear a
seção 4 para "Variáveis Aleatórias Contínuas" e destacar Cantor em subseção.

**G3. A medida de Lebesgue é introduzida e caracterizada duas vezes, a primeira
cedo demais.** — linhas 620–626 (subseção 1.3) e 938–951 (subseção 4.2).
Em 1.3, o encerramento da definição de espaço de medida já apresenta
$(\mathbb{R},\mathscr{B}(\mathbb{R}),\lambda)$ e a propriedade
$\lambda((a,b])=b-a$. Em 4.2, o `remark` `rem:medida-lebesgue-qtp` repete a
construção e reafirma exatamente a mesma propriedade. A primeira ocorrência é
prematura: surge antes de qualquer variável absolutamente contínua e usa Lebesgue
só como "outro exemplo de espaço de medida".
*Sugestão:* reduzir 622–626 a uma menção mínima com remissão à seção 4 e
concentrar a definição de $\lambda$, da $\sigma$-álgebra de Lebesgue e de
"quase todo ponto" em 4.2.

### MÉDIO

**M1. A subseção de Cantor está superdimensionada e usa pseudo-subseções.**
— 1179–1640 (≈460 linhas; comparação: a seção de caracterização inteira tem
~50 linhas). Reúne a construção iterativa da função (em prosa, fora de
ambiente), o experimento aleatório, a recursão de $F_X$, a unicidade e a
ausência de densidade, com cinco divisões feitas em `\noindent\textbf{...}`
(1270, 1348, 1464, 1492, 1615) em vez de `\subsubsection`, embora o preâmbulo
defina formatação para `subsubsection` (linha 64). Como são duas construções
concorrentes do mesmo objeto (determinística por aproximações $f_n$;
probabilística via $X$), falta também uma frase de roteiro ligando as duas.
*Sugestão:* ao separar a seção (G2), promover as divisões a `\subsubsection` e
acrescentar no início uma frase anunciando que se construirão $\mathcal{C}$ e
$X$ e que a identificação $F_X=\mathcal{C}$ virá da unicidade.

**M2. A "Recapitulação" recapitula toda a nota, mas está no meio dela.**
— 1642–1651 (subseção 4.7). Resume as seções 1–4, mas vem antes da seção 5
(densidades usuais) e da lista de exercícios; aninhada na seção 4, parece
resumir apenas as variáveis absolutamente contínuas.
*Sugestão:* promovê-la a seção própria e movê-la para o fim da parte expositiva
(depois da seção 5), ou reduzi-la a um parágrafo-ponte para as densidades usuais.

**M3. A subseção 1.3 mistura três temas e o título cobre só parte.** — 595–701.
Abre com espaço de medida (602–618), exemplo de Lebesgue e lei $\mu_X$
(620–647), depois exercício, átomo da lei (657–664), a observação sobre saltos
(666–674) e só no fim a fórmula de intervalos (679–700). O fio condutor
anunciado ("Antes de relacionarmos os saltos...") se cumpre apenas no terço
final.
*Sugestão:* desmembrar em "Átomos de uma lei" e "Probabilidades em intervalos",
ou mover o parágrafo de espaço de medida para o início de 4.2.

**M4. Exponencial e uniforme são reexibidas em seções diferentes.** — FD em
759–774 e 711–733 (seção 2); densidade da exponencial derivada em 901–931
(subseção 4.1); densidades em 1701–1739 (subseção 5.2). A exponencial aparece
em três lugares, a uniforme em dois. O exemplo de 4.1 funciona como duplicata
do de 5.2.
*Sugestão:* em 4.1, manter o exemplo como "exemplo-guia" mínimo e remeter por
`\eqref`/`\Cref` à seção 2 e a 5.2, sem reexibir a fórmula completa.

**M5. O TCD é enunciado por inteiro, mas só o corolário é usado; a subseção
funciona como apêndice no meio da narrativa.** — 1064–1107; uso em 1147–1150.
`thm-TCD` não é referenciado em nenhum ponto (o rótulo aparece só na definição);
a prova invoca `\Cref{cor-TCD}`. A justificativa declarada ("será usado na prova
seguinte") só se concretiza uma subseção depois.
*Sugestão:* enunciar apenas o corolário como ferramenta, derivando-o do TCD, ou
mover o par para dentro de 4.5 (ou para um apêndice), com frase de entrada e de
saída.

**M6. Exercícios de Cantor ficam sob o cabeçalho "Densidades usuais".** —
cabeçalho em 2218; `exercise:medida-cantor` 2275–2363 e
`exercise:construcao-cantor-avancada` 2366–2424. São 150 linhas de exercícios
sobre Cantor agrupadas indevidamente com os de densidades.
*Sugestão:* criar o cabeçalho "A função e a distribuição de Cantor" antes de
2275 e, se G2 for adotada, posicionar esse grupo junto à seção de Cantor.

**M7. Título da subseção 5.1 não corresponde ao da seção 5.** — 1656–1696.
"Um critério para construir densidades" não é uma densidade usual: é o critério
de existência (conversa de `def:va-continua`) que fundamenta a lista.
*Sugestão:* mover o critério para o fim da seção 4 (ou logo após a definição de
variável absolutamente contínua) e abrir a seção 5 diretamente na lista.

**M8. A subseção 5.5 é redundante e desloca o fechamento da seção 5.** —
1979–2010. Reexibe a integral gaussiana já enunciada em 5.3
(`eq:gaussiana-integral`, 1810–1815) e a normalização de Cauchy já calculada em
1834–1841; o único conteúdo novo é a ilustração com $g(x)=1/(1+x^2)$. Somada à
frase "Com isso encerramos a lista" (2103–2107), a seção tem três fechamentos
(1691–1696, 1973–1977, 2103–2107).
*Sugestão:* fundir 5.5 em 5.1/5.2 como um parágrafo, substituir a reexibição da
integral por remissão, e reescrever (ou remover) a frase de 2103–2107.

### MENOR

**m1. Figuras órfãs.** `fig:variavel-aleatoria` (399, a figura que ilustra a
definição de variável aleatória), `fig:aproximacoes-funcao-cantor` (1227),
`fig:construcao-cantor-distribuicao` (1310) e `fig:escolhas-cantor` (1410) não
são citadas por `\Cref`; o corpo usa "a figura" ou "a figura abaixo"
(1275, 1365). A convenção (§7–8) pede `\Cref` e integração da figura ao
discurso. *Sugestão:* inserir `\Cref{...}` nos parágrafos correspondentes.

**m2. Seções 2 e 3 sem subseções.** — 703 e 796. As seções 1, 4 e 5 têm
subseções; a 2 (dois exemplos, duas figuras) pediria "A distribuição uniforme" /
"A distribuição exponencial". A seção 3, com um único resultado, pode ficar como
está.

**m3. "Função de distribuição acumulada" registrada duas vezes.** — 445–446 e
883–884. Manter a justificativa em 4.1 (acumula a densidade) e reduzir a de 1.

**m4. Remissão prospectiva de Cantor parcialmente não cumprida.** — 1249–1250
anuncia que "a identificação precisa dos intervalos removidos" está nos
exercícios finais, mas nem `exercise:medida-cantor` nem o
`starredexercise` pedem explicitamente que os intervalos removidos sejam
identificados com os trechos em que $\mathcal{C}$ é constante (a remissão de
1237–1240, sobre convergência uniforme, essa sim é cumprida). *Sugestão:*
acrescentar um item ao exercício de Cantor ou ajustar a frase.

**m5. Rótulos não usados e convenção.** Vários labels de exercícios e figuras
não têm `\Cref` correspondente (natural nos exercícios). Dois rótulos fogem da
convenção `prefixo:`: `thm-TCD` e `cor-TCD` (1078, 1095) usam hífen. Como
`thm-TCD` não é referenciado, o de menor impacto é renomear `cor-TCD` para
`cor:convergencia-dominada`.

**m6. Agrupamento de exercícios.** `exercise:normalizacao-exponencial-modulo`
(2164) testa o teorema de caracterização, não é exemplo de FD; e
`exercise:densidade-valor-extremo` (2208) depende de derivar integral,
encaixando melhor no grupo das absolutamente contínuas.

---

## Rearranjo proposto (versão mínima)

Mantém a ordem atual e faz poucas movimentações:

1. **Funções de Distribuição** — definição, exemplo discreto, propriedades;
   separar 1.3 em "Átomos de uma lei" e "Probabilidades em intervalos"; enxugar
   a menção a Lebesgue (G3).
2. **Exemplos de Funções de Distribuição** — inalterada (opcional: duas
   subseções).
3. **Caracterização das Funções de Distribuição** — inalterada; acrescentar uma
   frase dizendo que a proposição 1.2 dá a necessidade e o teorema, a
   suficiência.
4. **Variáveis Aleatórias Absolutamente Contínuas** — definir densidade,
   concentrar aqui Lebesgue/"quase todo ponto", definir o critério de
   construção (M7), provar probabilidades de pontos e intervalos; o TCD entra
   como ferramenta anunciada, de preferência já reduzido ao corolário (M5).
5. **Distribuições Contínuas sem Densidade: o Exemplo de Cantor** — nova seção
   com as divisões promovidas a `\subsubsection` (M1 + G2).
6. **Algumas Funções de Densidade Usuais** — abrir com as densidades básicas;
   fundir 5.5 como parágrafo; manter beta–gama como fecho.
7. **Recapitulação** — seção curta imediatamente antes dos exercícios (M2).
8. **Exercícios propostos** — mover o exercício de 1.3 para cá e criar o
   cabeçalho "A função e a distribuição de Cantor" (G1 + M6).

Esse arranjo alinha os títulos ao conteúdo, elimina a duplicação de Lebesgue e
as reexibições de uniforme/exponencial, e resolve a numeração dos exercícios sem
reescrever nenhum argumento.

---

## Notas de método e limites

- A verificação das referências cruzadas foi feita sobre o `.tex` e o `.aux`:
  não há referência quebrada. As "referências para frente" listadas
  (`exercise:integral-gaussiana`, `exercise:funcao-gama-recorrencia`,
  `tab:densidades-usuais`) são intencionais e resolvem em duas compilações.
- Não foram avaliados fidelidade a Grimmett–Welsh, correção matemática,
  ortografia nem a aparência visual do PDF (para isso, ver `parecer.md` e os
  relatórios em `agent-output/`).
- As contagens de linhas nos achados seguem a numeração do arquivo atual e
  podem deslizar após a primeira edição.
