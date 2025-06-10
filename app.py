import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Konfigurer Flask-session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Databasekonfigurasjon – Bruk IP-en til din VM
db_config = {
    "host": "10.2.3.98",  # Bytt til riktig VM-IP
    "user": "sami1",
    "password": "IMKuben1337!",
    "database": "slap_users"
}

# Funksjon for å opprette databaseforbindelse
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Hjemmeside
@app.route('/')
def index():
    if 'user_id' in session:
        return render_template("quiz.html", username=session['username'])
    return redirect(url_for('login'))


# Registreringsside
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            flash("Registrering vellykket! Logg inn nå.", "success")
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash("Brukernavn eller e-post finnes allerede.", "danger")
    
    return render_template('register.html')

# Loginside
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash("Innlogging vellykket!", "success")
            return redirect(url_for('index'))
        else:
            flash("Feil brukernavn eller passord.", "danger")

    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("Du er nå logget ut.", "info")
    return redirect('/login')

# Restarte spillet
@app.route('/restart_quiz')
def restart():
    return render_template('quiz.html')

@app.route('/get_questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM quiz_db;")
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)





# Kjør appen
if __name__ == '__main__':
    app.secret_key = "supersecretkey"
    app.run(debug=True)
