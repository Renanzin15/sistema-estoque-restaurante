# 🍽️ Sistema de Controle de Estoque — Bar & Restaurante

> Sistema web para gestão de estoque de um bar e restaurante, desenvolvido em Python + Flask.
> **Status:** 🚧 Em desenvolvimento (projeto de estudo, evoluindo em módulos)

---

## 📌 Sobre o projeto

Sistema de gestão pensado a partir da necessidade real de um estabelecimento de **bar e restaurante**. O objetivo final é um sistema completo de operação (um "painel" onde o dono acompanha tudo), construído de forma incremental — um módulo por vez, começando pela fundação: o **controle de estoque**.

Um único cadastro de produtos, com uma **categoria** que separa os setores (**Bar** e **Cozinha**), permitindo gerir e filtrar os dois em um só lugar.

---

## ✅ Funcionalidades

**Já implementadas:**
- 📋 Listagem de produtos em estoque (nome, categoria, quantidade, unidade, preço)
- ➕ Cadastro de novos produtos por formulário
- 🏷️ Separação por setor (Bar / Cozinha)

**No roadmap:**
- ✏️ Editar e excluir produtos (CRUD completo)
- 🔍 Filtro por categoria
- ⚠️ Alerta de estoque baixo
- 💾 Persistência em banco de dados (SQLite)
- 🍷 Módulo de cardápio, mesas, pedidos e monitoramento
- 🎨 Interface visual finalizada

---

## 🛠️ Tecnologias

- **Python 3**
- **Flask** (framework web)
- **Jinja2** (templates)
- **HTML**

---

## ▶️ Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/Renanzin15/sistema-estoque-restaurante.git

# 2. Entre na pasta
cd sistema-estoque-restaurante

# 3. Instale o Flask
pip install flask

# 4. Rode a aplicação
python app.py
```

Depois é só abrir no navegador: **http://localhost:5000**

---

## 📁 Estrutura do projeto

```
sistema-estoque-restaurante/
├── app.py                 # Aplicação Flask (rotas e lógica)
├── templates/
│   ├── index.html         # Página inicial (lista de produtos)
│   └── adicionar.html     # Formulário de cadastro
├── README.md
└── .gitignore
```

---

## 👤 Autor

**Renan** — [@Renanzin15](https://github.com/Renanzin15)

> Projeto desenvolvido como estudo prático de desenvolvimento web com Python, escrito integralmente à mão como parte do meu aprendizado.
