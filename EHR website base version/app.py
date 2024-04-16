from flask import Flask, render_template, request, redirect, url_for, flash,session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///hospital.db', connect_args={'multi': True})

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pN8YdLyM42OCA4eTXp73lA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db = SQLAlchemy(app)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(200), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = db.text(f"SELECT * FROM Doctor WHERE username = '{username}' AND password = '{password}'")
        user = db.session.execute(query).fetchone()
        print(user)
        if user:
            session['id'] = user.id
            return jsonify(success=True), 200
        else:
            flash('Invalid username or password')
            return jsonify(success=False), 401
    return render_template('login.html')

@app.route('/search_patient', methods=['GET', 'POST'])
def search_patient():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name')
        sql = db.text(f"SELECT age,condition FROM patient WHERE name = '{patient_name}'")
        patients = db.session.execute(sql).fetchall()
        print(patients)
        return render_template('dashboard.html', patients=patients)

    return render_template('dashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if username already exists
        user_exists = Doctor.query.filter_by(username=username).first() is not None
        if user_exists:
            flash('Username already exists.')
            return redirect(url_for('register'))
        else:
            new_doctor = Doctor(username=username,password=password)
            db.session.add(new_doctor)
            db.session.commit()
            flash('Doctor registered successfully.')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        condition = request.form.get('condition')
        user_id=session['id']
        new_patient = Patient(name=name, age=age, condition=condition, doctor_id=user_id)
        db.session.add(new_patient)
        db.session.commit()
        flash('New patient added successfully.')
        return redirect(url_for('dashboard'))

    return render_template('add_patient.html')

def add_doctor(username, password):
    existing_doctor = Doctor.query.filter_by(username=username).first()
    if existing_doctor is None:
        new_doctor =  Doctor(username=username,password=password)
        db.session.add(new_doctor)
        db.session.commit()
        print(f'Added new doctor: {username}')
    else:
        print(f'Doctor with username {username} already exists.')

with app.app_context():
    db.create_all()
    add_doctor('yangLi', '100')
    add_doctor('yaoming', '1234')
