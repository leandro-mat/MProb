# MProb — Notas de Aula de Métodos Probabilísticos

![Compilar LaTeX](https://github.com/leandro-mat/MProb/actions/workflows/compilar.yml/badge.svg)

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

Os PDFs são **compilados automaticamente pelo GitHub Actions** a cada alteração
nos arquivos `.tex` ou `.bib` (badge de status acima). Não é preciso compilar
nem subir o PDF manualmente — a própria CI atualiza os PDFs no repositório.

Compilação manual (opcional), dentro da subpasta da nota:

```bash
latexmk -pdf sup-inf.tex
```

O PDF final sai na própria subpasta (ex.: `sup-inf/sup-inf.pdf`).

## Notas em PDF

Links diretos de download (funcionam sem conta no GitHub):

- [Supremos, ínfimos e completude da reta](https://github.com/leandro-mat/MProb/raw/main/sup-inf/sup-inf.pdf)

Para adicionar uma nova nota, basta criar a subpasta com o `.tex` principal
(e os capítulos) e enviar para o `main` — o GitHub Actions compila e o link
aparece aqui.

## Colaborações e Correções

Este material é mantido como um projeto aberto. Qualquer pessoa interessada
pode colaborar — com correções de erros de digitação, ajustes em demonstrações,
sugestões de conteúdo ou novas notas de aula.

### Regras básicas

- O repositório é **público**; qualquer um pode clonar, ler e abrir *issues*.
- A branch `main` é **protegida**: nada é commitado diretamente nela. Toda
  mudança entra por um *pull request* revisado e aprovado pelo professor.
- Mensagens de commit devem ser curtas e em português, descrevendo o que mudou.
- Nunca versione artefatos de compilação LaTeX (`.aux`, `.log`, `.out`, `.toc`,
  `.synctex.gz`, etc.) — o `.gitignore` já cuida disso.
- Mantenha a estrutura atual: cada nota de aula em sua própria subpasta, com os
  recursos compartilhados referenciados de `arquivos-aux/`.

### Antes de começar

1. Tenha uma conta no GitHub e o `git` instalado.
2. Obtenha o repositório de uma destas formas:
   - **Alunos da disciplina**: são adicionados como **colaboradores** com acesso
     de escrita. Envie seu usuário do GitHub para o professor, que o adiciona
     com:
     ```bash
     gh repo collaborator add <usuario-do-github> --permission push
     ```
   - **Demais interessados**: faça um *fork* do repositório e trabalhe a partir
     do seu fork.

### Fluxo para enviar uma correção

1. **Obtenha o código.** Para colaboradores:
   ```bash
   git clone https://github.com/leandro-mat/MProb.git
   ```
   Para quem usou fork: clone o seu fork e registre o repositório original como
   `upstream`:
   ```bash
   git clone https://github.com/<seu-usuario>/MProb.git
   cd MProb
   git remote add upstream https://github.com/leandro-mat/MProb.git
   ```

2. **Atualize a `main` e crie um branch** para a sua correção:
   ```bash
   git checkout main && git pull
   git checkout -b corrige-typo
   ```
   (quem usou fork, use `git pull upstream main` no passo de atualização)

3. **Edite** o arquivo da nota que deseja corrigir (ex.:
   `sup-inf/capitulos/capitulo1.tex`).

4. **Compile** para conferir que o documento continua válido:
   ```bash
   latexmk -pdf sup-inf.tex   # executar dentro de sup-inf/
   ```

5. **Commit** com uma mensagem descritiva em português:
   ```bash
   git add -A && git commit -m "corrige typo em capitulo1"
   ```

6. **Envie o branch**:
   ```bash
   git push -u origin corrige-typo
   ```

7. **Abra um pull request** no GitHub apontando para a branch `main` do
   repositório original, descrevendo o que foi alterado e por quê.

### Depois de abrir o PR

- A proteção do `main` exige **1 aprovação** — o professor revisará o PR.
- Responda a eventuais comentários de revisão e mantenha o PR atualizado
  (`git push` no mesmo branch).
- Após a aprovação, o PR é mesclado e você pode apagar o branch da correção.

### Sugestões sem código

Se você encontrou um erro mas prefere não editar, abra uma *issue* no GitHub
descrevendo o problema e a localização (nota, seção, página).

## Licença

Este material está licenciado sob a **Creative Commons
Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional**
(CC BY-NC-SA 4.0), como indicado no arquivo [`LICENSE`](LICENSE) e no rodapé
das notas de aula. Ao citar ou reutilizar, mencione a origem e o autor.
