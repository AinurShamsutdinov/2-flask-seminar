from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Enter number'
    }
    return render_template('ex-7/index.html', **context)


@app.post('/power/')
def power():
    number: float = float(request.form.get('number'))
    context = {
        'title': 'Power two of number',
        'number': number,
        'result': 2 ** number
    }
    return render_template('ex-7/result.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
