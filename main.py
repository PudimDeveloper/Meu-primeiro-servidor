from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
         "mensagem": "Oi, funcionando!",
         "mensagem2": "vá para /boasvindas",
         "status": 200
}

@app.route("/boasvindas")
def vindas():
     return {"mensagem": "Que rapido!"}

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
