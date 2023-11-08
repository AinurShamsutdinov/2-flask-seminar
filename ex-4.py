from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ex-4/index.html')


@app.post('/count/')
def count_words():
    text = request.form.get('text')
    list_words = text.split(' ')
    context = {
        'amount': len(list_words)
    }
    return render_template('ex-4/count.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
