from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index_page():
    try:
        a = int(request.form["a"])
        b = int(request.form["b"])
        summa = a + b
    except:
        a, b = 0, 0
        summa = "Не удалось вычислить сумму"
    return render_template("index.html", answer=summa, a=a, b=b)