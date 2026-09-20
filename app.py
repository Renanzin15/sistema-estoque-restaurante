from flask import Flask, render_template, request, redirect

app = Flask(__name__)

produtos= [
        {"nome": "Cerveja Heineken 600ml", "categoria": "Bar", "quantidade": 24, "unidade": "Garrafa", "preco": 8.50},

        {"nome":"Coca-Cola lata 350ml", "categoria": "Bar", "quantidade": 48, "unidade": "lata", "preco": 5.00},

        {"nome": "File Mignon", "categoria": "Cozinha", "quantidade": 12, "unidade": "kg", "preco": 62.90} 
    ]

@app.route("/")
def inicio():
    categoria = request.args.get("categoria")
    if categoria:
        lista = []
        for p in produtos:
            if p["categoria"] == categoria:
                lista.append(p)
    else:
        lista = produtos
    return render_template("index.html", lista_de_produtos=lista)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantidade"]
        unidade = request.form["unidade"]
        preco = request.form["preco"]

        novo_produto = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade,
            "unidade": unidade,
            "preco": preco,
        } 
        produtos.append(novo_produto)
        return redirect("/")
    return render_template("adicionar.html")

@app.route("/excluir/<int:indice>")
def excluir(indice):
    produtos.pop(indice)
    return redirect("/")

@app.route("/editar/<int:indice>", methods=["GET","POST"])
def editar(indice):
    if request.method == "POST":
        produtos[indice]["nome"] = request.form["nome"]
        produtos[indice]["categoria"] = request.form["categoria"]
        produtos[indice]["quantidade"] = request.form["quantidade"]
        produtos[indice]["unidade"] = request.form["unidade"]
        produtos[indice]["preco"] = request.form["preco"]
        return redirect("/")
    
    produto = produtos[indice]
    return render_template("editar.html", produto=produto, indice=indice)

if __name__ == "__main__":
    app.run(debug=True)