from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = {
            'name': request.form.get('name'),
            'email': request.form.get('email')
        }
        response = make_response(render_template('ex-9/user_page.html', **context))
        response.set_cookie('name', request.form.get('name'))
        response.set_cookie('email', request.form.get('email'))
        return response
    return render_template('ex-9/index.html')


@app.get('/exit/')
def logout():
    response = make_response(render_template('ex-9/index.html'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
