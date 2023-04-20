from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template("index.html")



if __name__ == '__main__':

    app.run(host="0.0.0.0",port=80)  