# 📓 Meu Progresso — Sistema de Estoque (Bar & Restaurante)

> Projeto de estudo em Python + Flask. Eu escrevo todo o código na mão; o Claude só ensina, corrige e roda.
> **Última atualização:** 19/09/2026

---

## 🎯 A visão do projeto
Construir um **sistema completo de gestão de restaurante** (um "simulador" onde eu sei tudo que acontece). Começo pelo **estoque** (a fundação) e vou crescendo em módulos:
Estoque → Cardápio → Mesas (com garçom e tempo de espera) → Pedidos → Monitoramento/Dashboard → Lista de tarefas → Front bonito no final.

**Regra de ouro:** um módulo de cada vez. Back-end primeiro, beleza depois.

---

## ✅ O que eu JÁ construí

### Fundação
- [x] App Flask rodando 100% local (`http://localhost:5000`)
- [x] Entendi rotas (`@app.route`), o servidor, e os logs (200, 404, 405, 302, 500)
- [x] Estrutura de HTML (head/body, h1, ul/li, semântica)
- [x] Templates: separei Python do HTML com `render_template` + pasta `templates/`
- [x] Reconstruí o app do zero sozinho (teste de memória) ✅

### Módulo 1 — Estoque (coração pronto!)
- [x] Modelo de dados: cada produto é um dicionário com `nome, categoria, quantidade, unidade, preco`
- [x] Lista de produtos exibida na tela com laço Jinja (`{% for %}`)
- [x] Categoria separando **Bar** e **Cozinha** (mesma lista, um sistema só)
- [x] Movi a lista pra **variável global** (pra os dados persistirem entre requests)
- [x] **Formulário de cadastro funcionando** (`/adicionar`) — adiciono produto pela tela! 🎉
  - Rota com `methods=["GET", "POST"]`
  - `request.form[...]` pra ler o que foi digitado
  - `.append()` pra adicionar na lista
  - `redirect("/")` pra voltar e ver o resultado
- [x] **Navegação entre páginas** com links `<a href="...">` (index ↔ adicionar)
- [x] **CRUD completo!** (Create, Read, Update, Delete)
  - 🗑️ **Excluir** produto — rota dinâmica `/excluir/<int:indice>` + `.pop(indice)` + `loop.index0` no link
  - ✏️ **Editar** produto — rota `/editar/<int:indice>` (GET mostra form preenchido com `value="{{ produto.campo }}"`, POST salva com `produtos[indice]["campo"] = request.form["campo"]`)
  - Aprendi **rotas dinâmicas**: `<int:indice>` captura um número da URL
- [x] **Filtro por categoria** (Bar / Cozinha / Todos) — links com `?categoria=...` na URL, lidos no Python com `request.args.get("categoria")` e filtrando a lista

---

## 🧠 Conceitos que aprendi
- **Rota** = liga um endereço a uma função
- **Template + ponte**: `render_template("x.html", apelido=variavel)` → o apelido tem que bater com o `{% for %}` do HTML
- **Jinja**: `{% %}` age (for/if), `{{ }}` mostra um valor
- **Dicionário**: `{"chave": valor}` — `:` liga chave e valor, `,` separa pares
- **Acessar campo**: sempre com **PONTO** → `produto.nome` (nunca underline)
- **Variável local vs global**: dentro da função morre a cada visita; global (na margem) fica viva
- **GET vs POST**: GET = pedir/ver página; POST = enviar/criar dados
- **Bug silencioso**: quando algo aparece vazio, é chave errada ou typo (o Jinja não avisa)

---

## 🐛 Meus erros mais comuns (pra não repetir!)
1. 💰 **Preço com vírgula** (`8,50`) → tem que ser **ponto** (`8.50`). *(errei umas 3x!)*
2. 🔤 **Acessar campo com underline** (`produto_nome`) → é **ponto** (`produto.nome`)
3. `{% for ... %}` → **esquecer o `%}`** no fim
4. Colocar código **fora da função** → cuidado com a **indentação** (espaços)
5. `true` → em Python é **`True`** (T maiúsculo)
6. Fechar `}` de dicionário **cedo demais** → um `{` no início, um `}` só no fim
7. Windows escondendo extensão → arquivo virou `.html.txt` (renomear no VS Code)
8. Tag HTML sem fechar o `>` no fim

---

## 📁 Estado atual dos arquivos
```
D:\Claude\estoque\
├── app.py                    ← Flask: rotas / e /adicionar, lista global de produtos
├── MEU_PROGRESSO.md          ← este arquivo
└── templates\
    ├── index.html            ← mostra a lista de produtos (laço Jinja)
    └── adicionar.html        ← formulário pra cadastrar produto
```

---

## 🐙 GitHub (portfólio)
- Repositório: **https://github.com/Renanzin15/sistema-estoque-restaurante** (público)
- Branch principal: `main`
- **Ciclo pra subir mudanças novas** (a cada avanço):
  ```bash
  git add .
  git commit -m "descreve o que fez"
  git push
  ```

---

## ▶️ Como rodar
1. Abrir o terminal na pasta `estoque`
2. Rodar: `python app.py`
3. Abrir no navegador: `http://localhost:5000`
4. Formulário: `http://localhost:5000/adicionar`
5. Salvou uma mudança? Só apertar **F5** (o `debug=True` recarrega sozinho)

---

## 🚧 ONDE A GENTE CONTINUA (próximo passo)
Eu terminei o **CRUD completo** (criar, listar, editar, excluir) + navegação + **filtro por categoria**. Os próximos passos, em ordem sugerida:

1. 💾 **Banco de dados (SQLite)** — pra os produtos **não sumirem** quando o servidor reinicia (essa é a "dor" que ainda tenho: hoje os dados vivem só na memória)
2. Depois: alerta de estoque baixo, e começar os próximos módulos (cardápio, mesas, pedidos)

> ⚠️ Lembrete: hoje, ao reiniciar o servidor, os produtos que adiciono pela tela **somem** (só voltam os 3 do código). Isso é esperado — é o banco de dados que vai resolver.

---

*Quando eu voltar, é só perguntar "onde a gente parou?" que o Claude me lembra a partir daqui.*
