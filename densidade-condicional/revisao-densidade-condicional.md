# Revisão de densidade-condicional.tex

Revisão realizada em 14 de outubro de 2026, seguindo
`../NOTACOES-E-CONVENCOES.md`. Foram examinados o texto completo, as
demonstrações, os exemplos, os exercícios e as 19 páginas do PDF recompilado.

## Cálculos e resultados

Os cálculos dos exemplos e exercícios estão corretos. Além da conferência
direta, foram verificadas simbolicamente 25 identidades, incluindo marginais,
normalizações, condicionais, o quadrado completo da normal e o jacobiano da
transformação usada no exercício sobre a soma de exponenciais.

| Modelo | Resultados conferidos |
|---|---|
| Conjunta `2 exp(-x-y)`, para `0<x<y` | Marginais exponencial de taxa 2 e `2 exp(-y)(1-exp(-y))`; condicionais exponencial deslocada e exponencial truncada; independência de `X` e `Y-X`. |
| Normal bivariada | Marginal normal padrão; média condicional `rho*x` e variância `1-rho²`; transformação para os parâmetros gerais e equivalência entre independência e `rho=0`. |
| Uniforme no triângulo | Marginal `2(1-x)`; condicional uniforme em `(0,1-x)`; probabilidade solicitada igual a `1/2`. |
| Conjunta `exp(-y)`, para `0<x<y` | Marginais exponencial de taxa 1 e gama de forma 2 e taxa 1; condicionais exponencial deslocada e uniforme em `(0,y)`. |
| Duas exponenciais de mesma taxa | Jacobiano igual a 1; conjunta de `X` e da soma; marginal gama da soma; condicional uniforme em `(0,a)`. |
| Uniforme no disco | Marginal proporcional ao comprimento da seção vertical; condicional uniforme e normalizações. |
| Modelo em duas etapas | Conjunta `1/x`; marginal `-ln(y)`; condicional inversa `1/[x*(-ln(y))]` e normalizações. |

As convenções da distribuição gama e o uso da convergência dominada foram
conferidos nas notas anteriores mencionadas no texto.

## Correções aplicadas

1. Na introdução, as hipóteses de continuidade e positividade foram
   localizadas no ponto de condicionamento, em acordo com a proposição.
2. A verificação de que a condicional é uma densidade agora inclui a
   demonstração da continuidade de `G`, que já era anunciada no texto.
   Nos argumentos com convergência dominada, a função dominante ficou explícita.
3. Na observação sobre independência, a igualdade entre as condicionais e
   a marginal foi corretamente formulada para quase todo `x` e quase todo
   `y`. Foi distinguido o caso em que escolhemos uma conjunta fatorada
   pontualmente.
4. A afirmação sobre `Y-x` no primeiro exemplo passou a explicitar que se
   refere à distribuição condicional dado `X=x`.
5. No caso geral da normal, foi corrigida a descrição do sinal do expoente:
   ele é `-Q(x,y)/2`. A conclusão de que a independência força `rho=0` agora
   é justificada pela expressão já calculada da média condicional.
6. No triângulo e no disco, a conjunta passou a valer zero na fronteira,
   com uma explicação da irrelevância dessa escolha para as probabilidades.
   Isso compatibiliza pontualmente as conjuntas com as marginais e
   condicionais apresentadas, sem alterar as distribuições dos modelos.
7. A densidade transformada no exercício da soma é descrita como
   independente de `u` **no suporte**. Foi acrescentada a conferência da
   normalização da condicional uniforme.
8. Foram corrigidas concordância, acentuação, uma referência incorreta à
   subseção anterior e a distinção entre densidade e distribuição. Também
   foram ajustadas legendas, a escrita decimal na legenda da normal e o
   ambiente de uma fórmula que usava `$$`.
9. Na revisão das alterações posteriores do autor, foi explicitado que o
   conjunto `Z={x:f_X(x)=0}` tem probabilidade nula para a distribuição de
   `X`, sem exigir que tenha medida de Lebesgue nula. A explicação da
   extensão por 0 passou a usar `P(X∈Z)=∫_Z f_X=0` e o fator marginal da
   fórmula total. O comentário sobre continuidade foi mantido em um
   parágrafo próprio, esclarecendo que o limite das probabilidades em
   faixas é o valor `G(y)` da função de distribuição condicional.

## Convenção para as marginais, aprovada e aplicada

A definição original de densidade condicional exigia apenas `f_X(x)>0`,
mas a proposição seguinte necessitava também da igualdade

```tex
\int_{-\infty}^{\infty} f_{X,Y}(x,v)\,dv = f_X(x).
```

Para uma versão arbitrária da marginal, essa igualdade vale apenas em
quase todo ponto. Portanto, apenas aquelas hipóteses não garantiam
que o quociente fosse uma densidade em **cada** ponto admitido.

Um exemplo simples: tome a conjunta uniforme no quadrado `(0,1)²` e a
marginal de `X` igual a 1 em `(0,1)`, exceto em `x=1/2`, onde atribuímos o
valor 2. Essa função ainda é uma densidade da mesma marginal. Entretanto,
o quociente entre a conjunta e essa marginal, em `x=1/2`, integra `1/2`.

A solução aprovada pelo autor foi declarar, antes da proposição do limite,
a seguinte convenção:

```tex
Ao longo destas notas, escolhemos as densidades marginais por integração
da densidade conjunta, sempre que a integral correspondente for finita:
\[
  f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,v)\,dv,
  \qquad
  f_Y(y)=\int_{-\infty}^{\infty} f_{X,Y}(u,y)\,du.
\]
Essas integrais são finitas em quase todo ponto. Nos pontos excepcionais
em que uma dessas integrais for infinita, atribuímos o valor 0 à marginal
correspondente. Usaremos o quociente
que define a densidade condicional apenas nos pontos em que a marginal
é estritamente positiva e finita.
```

Com essa escolha, a definição agora exige `0<f_X(x)<∞`, e a normalização
vale em cada ponto admitido por construção. A identidade usada na
proposição seguinte deixou de ser uma hipótese adicional. A prova e a
explicação posterior foram ajustadas à mesma convenção.

Para escrever a fórmula total, a função condicional foi estendida por 0
nos pontos em que a marginal vale 0. O texto explica que a fatoração da
conjunta então vale em quase todo ponto do plano, o que justifica a
integração em `x`, inclusive quando a integral de uma seção é infinita.

A definição por quociente dispensa continuidade. As hipóteses de
continuidade da proposição servem para justificar sua interpretação pelo
limite das probabilidades em faixas. Essa distinção foi explicitada
junto à definição. Na prova do limite, a integrabilidade local das seções
foi justificada pela comparação com a marginal.

A observação sobre unicidade foi mantida e esclarecida: fixar a marginal
por integração garante a normalização pontual, mas outra versão da
conjunta ainda pode alterar a condicional em valores excepcionais de `x`.

## Validação

- `latexmk -pdf -interaction=nonstopmode -halt-on-error
  densidade-condicional.tex` concluiu a compilação, com duas passagens de
  `pdflatex` após as alterações.
- O log final não contém erros, referências ou citações indefinidas,
  referências duplicadas, caixas excedentes ou caixas insuficientemente
  preenchidas.
- O PDF final tem 19 páginas. Os trechos alterados para incorporar a
  convenção das marginais foram conferidos visualmente após a recompilação.
- O preâmbulo, a ordem das seções, os modelos probabilísticos e os
  resultados numéricos foram preservados.

A questão conceitual da definição foi resolvida com a convenção aprovada
pelo autor. Não há ajustes pendentes deste ponto da revisão.
