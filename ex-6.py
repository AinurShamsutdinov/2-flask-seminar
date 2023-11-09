from flask import Flask, render_template, request, Response, abort

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('ex-6/index.html')


@app.post('/userpage/')
def user_page():
    name = request.form.get('userName')
    age = int(request.form.get('userAge'))
    context = {
        'name': name
    }
    if age >= 18:
        return render_template('ex-6/user-page.html', **context)
    else:
        abort(400)


@app.errorhandler(400)
def age_not_appropriate(e):
    context = {
        'title': 'Age is not appropriate',
        'message': f'Age is not appropriate, should be above or equal to 18 years.'
    }
    return render_template('400.html', **context), 400


if __name__ == '__main__':
    app.run(debug=True)
