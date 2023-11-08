from flask import Flask, render_template, request

app = Flask(__name__)

_login = 'user'
_password = 'pass'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login/')
def login():
    return render_template('ex-3/login.html')


@app.post('/login/')
def process_login():
    user = request.form.get('user')
    password = request.form.get('password')
    if user.__eq__(_login) and password.__eq__(_password):
        return render_template('ex-3/start.html')
    else:
        raise ValueError('Your login or password are not good enough to login.')


@app.errorhandler(404)
def page_not_found(e):
    context = {
        'title': 'Wrong login or password',
        'url': request.base_url
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
