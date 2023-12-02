from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wordle')
def wordle():
    return render_template('wordle.html')


if __name__ == '__main__':
    app.run()
