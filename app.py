from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

users = {
    'jose': '1234',
    'andres': '1234'
}

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username 
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('bienvenido'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/bienvenido')
def bienvenido():
    if 'username' in session:
        username = session['username']
        return render_template('bienvenido.html', username=username)
    else:
        flash('Por favor, inicie sesión primero', 'warning')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Cerraste sesión exitosamente', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
