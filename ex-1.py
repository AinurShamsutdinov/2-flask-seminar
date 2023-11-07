from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'it works'


@app.get('/user/')
def user():
    return render_template('/ex-1/form.html')


@app.post('/hello/')
def greeting():
    user_name = request.form.get('name')
    return f'Hello {user_name}!'


if __name__ == '__main__':
    app.run(debug=True)
