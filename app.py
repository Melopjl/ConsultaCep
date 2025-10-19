from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        cep = request.form.get("cep")
        if cep:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)

            if response.status_code == 200:
                resultado = response.json()
            else:
                resultado = {"erro": "CEP não encontrado"}
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
