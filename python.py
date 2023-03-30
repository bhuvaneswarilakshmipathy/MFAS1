from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

rrn = {1: 2, 2: 0, 3: 1, 4: 3, 5: 5, 6: 1, 7: 6, 8: 0, 9: 1, 10: 0, 11: 2, 12: 1}
lista = random.sample(list(rrn.keys()), 4)
listb = [rrn[x] for x in lista]

@app.route('/')
def homepage():
    return render_template('registration.html', lista=lista)

@app.route('/login', methods=["POST"])
def login():
    password1 = request.form["passw1"]
    password2 = request.form["passw2"]
    password3 = request.form["passw3"]
    password4 = request.form["passw4"]
    password = password1+" "+password2+" "+" "+password3+" "+password4
    listpass = list(map(int, password.split()))

    if listpass == listb:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

@app.route('/failure')
def failure():
    return 'Incorrect username or password'

if __name__ == "_main_":
    app.run(debug=True,host='0.0.0.0')