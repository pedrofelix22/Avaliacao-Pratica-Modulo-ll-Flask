from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.get("/api/soma/<int:num1>/<int:num2>")
def soma (num1,num2):
    resultado = num1 + num2 
    return jsonify(resultado)

@app.get("/api/subtração/<int:num1>/<int:num2>")
def subitração (num1,num2):
    resultado = num1 - num2 
    return jsonify(resultado)


@app.get("/api/divisão/<int:num1>/<int:num2>")
def divisão (num1,num2):
    if num2 == 0:
        return jsonify({"erro":"Não e possivel divider por zero"})
    resultado = num1 / num2 
    return jsonify(resultado)


@app.get("/api/multiplicação/<int:num1>/<int:num2>")
def multiplicação (num1,num2):
    resultado = num1 * num2 
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
