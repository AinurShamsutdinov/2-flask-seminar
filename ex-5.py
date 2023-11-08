from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('ex-5/index.html')


@app.post('/calc')
def count():
    number = request.form.get('numberOne')
    num_one = int(number)
    num_two = int(request.form.get('numberTwo'))
    operation = request.form.get('operation')
    result = 'Something was not Ok'
    match operation:
        case '+':
            result = str(num_one + num_two)
        case '-':
            result = str(num_one - num_two)
        case '*':
            result = str(num_one * num_two)
        case '/':
            result = str(num_one / num_two)
    context = {
        'title': 'Result of calculation',
        'result': result,
        'operation': operation
    }
    return render_template('ex-5/count.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
