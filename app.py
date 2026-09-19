from flask import Flask, render_template, request, redirect

app = Flask(__name__)

produtos= [
        {"nome": "Cerveja Heineken 600ml", "categoria": "Bar", "quantidade": 24, "unidade": "Garrafa", "preco": 8.50},

        {"nome":"Coca-Cola lata 350ml", "categoria": "Bar", "quantidade": 48, "unidade": "lata", "preco": 5.00},

        {"nome": "File Mignon", "categoria": "Cozinha", "quantidade": 12, "unidade": "kg", "preco": 62.90} 
    ]

@app.route("/")
def inicio():

    return render_template("index.html", lista_de_produtos=produtos)

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

if __name__ == "__main__":
    app.run(debug=True)