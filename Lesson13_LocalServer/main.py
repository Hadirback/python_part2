from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/secret_page")
def secret_page():
    with open('key.txt', encoding='UTF-8') as f:
        correct_key = f.read()

    if request.args['key'] == correct_key:
        return render_template('secret_page.html')
    else:
        return "Incorrect Key!"


if __name__ == "__main__":
    app.run()
