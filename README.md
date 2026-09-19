<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B5CF6,100:A78BFA&height=190&section=header&text=Gest%C3%A3o%20de%20Restaurante&fontColor=ffffff&fontSize=44&fontAlignY=38&desc=Controle%20de%20Estoque%20%C2%B7%20Flask&descAlignY=60&descSize=18" width="100%" alt="Gestão de Restaurante" />

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-A78BFA?style=for-the-badge)

</div>

Sistema web para **gestão de um bar e restaurante**, desenvolvido em **Python + Flask** e construído de forma incremental — um módulo por vez, começando pela fundação: o **controle de estoque**.

## 📌 Sobre o projeto

O objetivo final é um sistema completo de operação (um "painel" onde o dono acompanha tudo). Começo pelo estoque: um único cadastro de produtos, com uma **categoria** que separa os setores (**Bar** e **Cozinha**), permitindo gerir e filtrar os dois em um só lugar. É o meu projeto para praticar back-end do zero e evoluir passo a passo.

## ✅ Funcionalidades

**Já implementadas**
- 📋 Listagem de produtos (nome, categoria, quantidade, unidade, preço)
- ➕ Cadastro de novos produtos por formulário
- 🏷️ Separação por setor (Bar / Cozinha)

**No roadmap**
- ✏️ Editar e excluir produtos (CRUD completo)
- 🔍 Filtro por categoria
- ⚠️ Alerta de estoque baixo
- 💾 Persistência em banco de dados (SQLite)
- 🍷 Módulos de cardápio, mesas, pedidos e monitoramento
- 🎨 Interface visual finalizada

## 🛠️ Tecnologias

- **Python 3**
- **Flask** (framework web)
- **Jinja2** (templates)
- **HTML**

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

## 👤 Autor

**Renan Santana** — Desenvolvedor · Python
[Portfólio](https://renanzin15.github.io) · [LinkedIn](https://www.linkedin.com/in/renan-santana-8508622a8/) · [GitHub](https://github.com/Renanzin15)

> Projeto desenvolvido como estudo prático de desenvolvimento web com Python, construído passo a passo para eu aprender e entender cada parte do código.

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:A78BFA,100:8B5CF6&height=110&section=footer" width="100%" alt="footer" />
</div>
