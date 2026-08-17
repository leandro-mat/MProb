# Notações e convenções das notas de probabilidade

Guia de continuidade notacional, editorial e LaTeX para
<code>prop-prob.tex</code> e para as próximas notas traduzidas ou adaptadas do
livro de Grimmett.

**Estado do documento:** guia vivo, atualizado em agosto de 2026.

Quando este arquivo e o código-fonte divergirem, o código-fonte atual deve ser
consultado antes de editar. Se a divergência resultar de uma decisão nova,
atualize também este guia.

## 1. Princípios gerais

- O texto é escrito em português brasileiro, com linguagem clara e gradual.
  A intuição vem antes da formalização sempre que isso ajudar o leitor.
- A terminologia matemática deve ser mantida estável entre as seções.
- Conceitos que ainda não foram definidos não devem ser usados como se já
  fossem familiares. Em particular, introduza independência, variáveis
  aleatórias, esperança etc. somente quando a organização do texto chegar a
  esses conceitos.
- Exemplos concretos — moedas, dados, conjuntos finitos e inteiros — servem
  para apresentar a ideia antes do tratamento abstrato.
- Os números impressos de teoremas, exemplos e exercícios são gerados pelo
  LaTeX. Não os fixe manualmente no texto.

## 2. Modelo probabilístico básico

| Notação | Significado e uso |
|---|---|
| \(\mathcal{E}\) | Experimento aleatório ou experimento cujo resultado não é completamente predeterminado. |
| \(\Omega\) | Espaço amostral: conjunto cujos elementos representam os resultados possíveis de \(\mathcal{E}\). |
| \(\omega\), \(\omega_i\) | Um resultado, ou ponto, de \(\Omega\). Em lançamentos infinitos, \(\omega=(\omega_1,\omega_2,\ldots)\) também denota uma sequência completa de resultados. |
| \(A,B,C,E\) | Eventos, isto é, subconjuntos de \(\Omega\). Para famílias de eventos, use normalmente \(A_i\), \(B_i\), etc. Embora \(E\) apareça em explicações introdutórias, \(A,B,C\) são as letras preferidas para eventos genéricos. |
| \(\mathcal{F}\) | Coleção de eventos; formalmente, uma \(\sigma\)-álgebra de subconjuntos de \(\Omega\). |
| \(\mathscr{P}(\Omega)\) | Conjunto das partes de \(\Omega\), isto é, a coleção de todos os seus subconjuntos. |
| \((\Omega,\mathcal{F})\) | Espaço mensurável. |
| \(\mathbb{P}\) | Medida de probabilidade sobre \((\Omega,\mathcal{F})\). Para \(A\in\mathcal{F}\), \(\mathbb{P}(A)\) é a probabilidade do evento \(A\). |
| \((\Omega,\mathcal{F},\mathbb{P})\) | Espaço de probabilidade. |
| \(\mathbb{Q}\) | Segunda medida de probabilidade, quando é necessário comparar duas medidas. Não usar essa letra para introduzir os racionais sem esclarecer o contexto. |

Um evento ocorre quando o resultado efetivo do experimento pertence ao
subconjunto que o representa. Assim, não se deve confundir um resultado
\(\omega\in\Omega\) com um evento \(A\subseteq\Omega\). Em espaços
discretos, escrevemos por abuso conveniente
\[
\mathbb{P}(\omega):=\mathbb{P}(\{\omega\}),
\]
quando o contexto deixa claro que se trata do evento unitário.

## 3. Notação de conjuntos

| Notação | Convenção |
|---|---|
| \(\varnothing\) | Conjunto vazio. O preâmbulo também faz <code>\emptyset</code> produzir o mesmo símbolo, mas <code>\varnothing</code> é a forma preferida nos novos trechos. |
| \(A\subseteq B\) | \(A\) é subconjunto de \(B\), sem exigir que a inclusão seja própria. |
| \(A^c\) | Complementar de \(A\) relativo a \(\Omega\). Também se escreve \(\Omega\setminus A\) quando o universo precisa ficar explícito. |
| \(A\setminus B\) | Diferença: elementos de \(A\) que não pertencem a \(B\). |
| \(A\triangle B\) | Diferença simétrica: \((A\setminus B)\cup(B\setminus A)\). |
| \(A\cap B\), \(A\cup B\) | Interseção e união. |
| \(\#A\) | Cardinalidade de \(A\), especialmente em espaços finitos. |
| \(A_i\cap A_j=\varnothing\), \(i\ne j\) | Os eventos são dois a dois disjuntos. |

Preferimos <code>:=</code> para introduzir uma definição e <code>=</code> para
uma identidade ou igualdade já estabelecida. O código antigo ainda contém
alguns usos de <code>\equiv</code>; não reproduza esse padrão em novos
trechos sem uma razão específica.

Para famílias enumeráveis, use a notação explícita
\[
\bigcup_{i=1}^{\infty}A_i,
\qquad
\bigcap_{i=1}^{\infty}A_i,
\qquad
\sum_{i=1}^{\infty}\mathbb{P}(A_i).
\]
Quando a família for dois a dois disjunta, mantenha essa expressão no texto;
ela é a terminologia adotada nas notas.

Nas notas, \(\mathbb{N}\) é usada normalmente para os índices positivos
\(\{1,2,3,\ldots\}\). Se for necessário incluir o zero, escreva o conjunto
explicitamente ou introduza essa convenção no trecho correspondente.
## 4. Notações de modelos já utilizados

### Dados

O exemplo do dado usa inicialmente
\[
\Omega=\{1,2,3,4,5,6\},
\]
mas também apresenta, para enfatizar a generalidade da teoria, o espaço
amostral formado pelos ícones <code>\faDiceOne</code> até
<code>\faDiceSix</code>. Dentro de fórmulas, os ícones devem ser envolvidos
por <code>\text{...}</code>. A notação
<code>\widetilde{\Omega}</code> aparece apenas para a alternativa ilustrativa;
a notação principal continua sendo \(\Omega\), sem til.

### Lançamentos infinitos de uma moeda

No modelo de lançamentos infinitos,
\[
\Omega=\{0,1\}^{\mathbb{N}},
\qquad
\omega=(\omega_1,\omega_2,\ldots),
\]
com \(1\) representando cara e \(0\) representando coroa.

- <code>\cara</code> é o macro para o ícone de cara
  (<code>\faSmile</code>).
- <code>\coroa</code> é o macro para o ícone de coroa
  (<code>\faCrown</code>).
- \(C(a_1,\ldots,a_k)\) denota um cilindro: as primeiras \(k\) coordenadas
  são fixadas e as demais ficam livres.
- O símbolo <code>*</code> representa uma coordenada livre.
- A medida nos cilindros é \(\mathbb{P}(C)=2^{-k}\) quando \(k\) coordenadas
  estão fixadas; a \(\sigma\)-álgebra é indicada por
  \(\mathcal{F}=\sigma(\text{cilindros})\).

### Distribuição zeta

Para \(s>1\), usamos
\[
\Omega=\{1,2,3,\ldots\},
\qquad
\mathbb{P}(A)=\frac{1}{\zeta(s)}\sum_{n\in A}\frac{1}{n^s},
\]
com \(\mathcal{F}=\mathscr{P}(\Omega)\). A massa de um ponto é escrita
\[
\mathbb{P}(\{n\})=\frac{1}{n^s\zeta(s)}.
\]
O parâmetro da distribuição é \(s\); não o confunda com o índice de uma
sequência ou com a variável de uma soma.

### Medidas de Gibbs

O módulo <code>medidas-gibbs.tex</code>, incluído no arquivo principal por
<code>\input{medidas-gibbs}</code>, usa as seguintes convenções:
\[
H:\Omega\longrightarrow\mathbb{R},
\qquad
Z(\beta)=\sum_{\omega\in\Omega}e^{-\beta H(\omega)},
\qquad
\mathbb{P}_{\beta}(A)=\frac{1}{Z(\beta)}
\sum_{\omega\in A}e^{-\beta H(\omega)}.
\]
Aqui \(H\) é o Hamiltoniano, \(Z\) é a função de partição e \(\beta>0\)
é o inverso da temperatura. Para o limite de baixa temperatura, usam-se
\[
h_{\min}=\min_{\omega\in\Omega}H(\omega),
\qquad
\Omega_{\min}=\{\omega\in\Omega:H(\omega)=h_{\min}\}.
\]
## 5. Terminologia e estilo do texto

- Use **espaço amostral**, **evento**, **\(\sigma\)-álgebra**, **espaço
  mensurável**, **medida de probabilidade** e **espaço de probabilidade**
  como termos principais.
- “Espaço de eventos” pode aparecer em explicações informais como sinônimo da
  coleção \(\mathcal{F}\), mas nas definições formais prefira
  “\(\sigma\)-álgebra”.
- Prefira **aditividade enumerável** ou **\(\sigma\)-aditividade**. “Aditividade
  contável”/“contavelmente aditiva” pode ser apresentada como sinônimo quando
  isso ajudar na tradução, mas não alterne as expressões sem necessidade.
- Use **enumerável** para uma coleção que pode ser posta em bijeção com um
  subconjunto de \(\{1,2,3,\ldots\}\), e **não enumerável** para o caso oposto.
- Para disjointness, use **dois a dois disjuntos** quando a condição for
  \(A_i\cap A_j=\varnothing\) para \(i\ne j\).
- Use **conjunto das partes**, e não introduza uma tradução diferente para
  \(\mathscr{P}(\Omega)\).
- Termos definidos pela primeira vez devem aparecer em <code>\emph{...}</code>
  quando isso contribuir para a leitura.
- A prosa usa aspas tipográficas de LaTeX: “texto entre aspas”. Números
  decimais seguem a convenção brasileira, por exemplo
  <code>0{,}000886</code>.
- Não antecipe conceitos ou resultados apenas para reproduzir uma tradução
  literal; adapte a exposição à ordem pedagógica das notas.

## 6. Ambientes, numeração e referências

O preâmbulo define os seguintes ambientes:

- <code>theorem</code>, <code>definition</code>, <code>example</code>,
  <code>proposition</code>, <code>corollary</code>, <code>lemma</code> e
  <code>remark</code> compartilham o mesmo contador;
- <code>exercise</code> possui contador próprio;
- <code>property</code> e <code>solution</code> são ambientes sem numeração.

Use títulos opcionais apenas para nomes, por exemplo:

~~~tex
\begin{proposition}[Produto de Euler]\label{prop:euler}
...
\end{proposition}
~~~

Não use o argumento opcional para inserir manualmente números como
<code>[1.23]</code>. Deixe a numeração natural do LaTeX continuar funcionando,
mesmo quando o <code>label</code> mantiver uma referência ao número original do
livro.

### Prefixos de <code>label</code>

Use nomes descritivos e estáveis:

| Objeto | Prefixo recomendado |
|---|---|
| Teorema | <code>thm:</code> |
| Definição | <code>def:</code> |
| Proposição | <code>prop:</code> |
| Corolário | <code>cor:</code> |
| Lema | <code>lem:</code> |
| Exemplo | <code>ex:</code> |
| Exercício | <code>exercise:</code> ou o prefixo já usado na subseção correspondente |
| Equação | <code>eq:</code> |
| Figura | <code>fig:</code> |

Coloque o <code>\label</code> logo depois de <code>\begin{...}</code> ou depois
de <code>\caption{...}</code> no caso de figuras. Referencie objetos com
<code>\Cref{...}</code> ou <code>\cref{...}</code>; isso mantém a numeração, o
nome do objeto e o link clicável corretos quando o texto crescer ou for
reorganizado.

Não escreva referências rígidas como “Exemplo 1.16” ou “Figura 7” no corpo do
texto. Escreva, por exemplo, <code>\Cref{ex:1.16}</code> e
<code>\Cref{fig:telescopia}</code>. Para equações, use
<code>\eqref{eq:nome}</code>.


## 7. Convenções LaTeX e de figuras

- Para matemática em linha, prefira <code>\(...\)</code>; para matemática
  destacada, <code>\[...\]</code>. Use <code>aligned</code>,
  <code>alignedat</code> ou <code>align</code> para expressões longas.
- Use <code>\mathbb</code> para conjuntos e medidas como
  <code>\mathbb{R}</code>, <code>\mathbb{N}</code> e <code>\mathbb{P}</code>;
  use <code>\mathcal</code> para estruturas como
  <code>\mathcal{E}</code> e <code>\mathcal{F}</code>; use
  <code>\mathscr</code> para <code>\mathscr{P}</code>.
- O preâmbulo redefine <code>\leq</code>, <code>\le</code>, <code>\geq</code>
  e <code>\ge</code> para as versões inclinadas. Use os comandos usuais; o
  estilo final será aplicado automaticamente.
- Em texto corrido, <code>\tfrac</code> costuma produzir frações mais
  discretas; em fórmulas centrais, use <code>\frac</code> quando a legibilidade
  pedir mais altura.
- Equações novas devem usar a numeração automática de
  <code>equation</code>/<code>align</code> e um <code>\label</code>; evite
  <code>\tag</code> manual.
- Diagramas são preferencialmente feitos com TikZ ou PGFPlots, com legendas em
  português e <code>\label</code> depois da legenda. Use <code>\Cref</code> no
  texto para chamá-los.
- Use <code>[H]</code> apenas quando a proximidade da figura com a demonstração
  ou o exemplo for pedagogicamente importante; caso contrário, prefira
  <code>[htbp]</code>.
- Ao ampliar a geometria de um TikZ sem ampliar as fontes, use
  <code>transform shape=false</code>. Evite caixas brancas atrás de rótulos
  quando elas prejudicarem sombreamentos ou padrões.
- Mantenha o estilo visual sóbrio: linhas finas, tons de cinza e, quando
  necessário, a cor <code>teal</code> já definida no preâmbulo.

## 8. Fluxo de trabalho para novas edições

1. Leia a região atual de <code>prop-prob.tex</code> antes de editar; o arquivo
   pode ter recebido alterações de outro colaborador.
2. Preserve as alterações existentes e ancore edições em <code>label</code>s ou
   em trechos textuais estáveis, não em números impressos de página ou de
   exemplo.
3. Após mudanças estruturais, compile pelo menos duas vezes para atualizar
   referências cruzadas. O comando usual é:

   ~~~sh
   latexmk -pdf -interaction=nonstopmode -halt-on-error prop-prob.tex
   ~~~

4. Verifique referências, caixas excedentes e a aparência de figuras. Quando o
   PDF for atualizado no repositório, ele deve corresponder ao <code>.tex</code>
   compilado.
5. Se uma nova decisão alterar uma notação ou uma convenção de estilo, registre-a
   neste arquivo para que os próximos agentes não precisem inferi-la do código.
