from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome_page():
    return render_template("index.html")


@app.route("/page2", methods=['POST'])
def second_page():
    nome = request.form["nome"]
    return render_template("welcome.html", html_data=nome)


if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
