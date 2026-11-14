from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify(
            {
                "empresa": "CodeFactory Solutions",
                "mensagem": "Sistema Funcionando !",
                "status": "sucesso",
            }
        )

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app


app = create_app()

@app.route("/sobre")
def sobre():
    return jsonify(
        {
            "projeto": "CodeFactory DevOps",
            "Versão": "1.0",
            "Descrição": "Projeto de Demostração DevOps",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
