from flask import Flask, render_template, request, flash, redirect, url_for
import secrets

app = Flask(__name__)

# secrets.token_hex()
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    name = request.form.get('name')
    if request.method == 'POST':
        if not request.form['name']:
            flash('Enter name!', 'danger')
            return redirect(url_for('form'))
        message = f'Hi, {name}!'
        flash(message, 'success')
        return redirect(url_for('form'))
    return render_template('ex-8/form.html')


if __name__ == '__main__':
    app.run(debug=True)
