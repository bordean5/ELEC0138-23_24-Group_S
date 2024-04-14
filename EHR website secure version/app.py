from flask import Flask, render_template, request, redirect, url_for, flash,session, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

from two_factor_verification import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pN8YdLyM42OCA4eTXp73lA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

limiter = Limiter(  #local limter, limter the access frequency, block brute force and dos attack 
    app=app,
    key_func=get_remote_address,  
    default_limits=["200 per day", "50 per hour"] 
)

def apply_security_headers(response):   #secuity defence headers to multiple attacs
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer-when-downgrade"
    return response

@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))

class Doctor(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/send_2fa', methods=['POST'])
@limiter.limit("10 per minute")
def send_2fa():
    username = request.form['username']
    password = request.form['password']
    user = Doctor.query.filter_by(username=username).first()
    if user and user.check_password(password):
        code =generate_code_secure()
        send_email(user.email,  "http://127.0.0.1:5000",code)
        session['2fa_code'] = code
        session['code_created_time'] = time.time() 
        session['code_attempts'] = 0 

        return jsonify({'message': '2FA code sent'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        code = request.form['code']
        user = Doctor.query.filter_by(username=username).first()
         
        if '2fa_code' in session and 'code_created_time' in session and 'code_attempts' in session: 
            session['code_attempts'] += 1
            current_time = time.time()
            if current_time - session['code_created_time'] > 300 or session['code_attempts'] >3:
                session.pop('2fa_code', None)
                session.pop('code_created_time', None)
                session.pop('code_attempts', None)
                return jsonify({'success': False, 'message': '2FA expired. Please generate a new one.'})

            if user and user.check_password(password) and '2fa_code' in session and code == str(session['2fa_code']):
                login_user(user)
                session.pop('2fa_code', None)
                session.pop('code_created_time', None)
                session.pop('code_attempts', None)
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'message': 'Invalid 2FA code. Please try again.' })
        else:
            return jsonify({'success': False, 'message': 'No 2FA code found. Please generate 2FA code first.'})
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    user_id = current_user.id
    user = Doctor.query.get(user_id)
    if user:
        return render_template('home.html', user=user)
    return render_template('home.html')


@app.route('/search')
@login_required
def search():
    return render_template('search.html')


@app.route('/search_results')
@login_required
def search_results():
    query = request.args.get('patient_name')
    results = Patient.query.filter(Patient.name.ilike(f'%{query}%')).all()
    return render_template('search_results.html', results=results)


@app.route('/case')
@login_required
def case():
    patients = Patient.query.filter_by(doctor_id=current_user.id).all()
    doctor_id = current_user.id
    return render_template('case.html', patients=patients, doctor_id=doctor_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email= request.form.get('email')
        # Check if username already exists
        user_exists = Doctor.query.filter_by(username=username).first() is not None

        if user_exists:
            flash('Username already exists.')
            return redirect(url_for('register'))
        else:
            new_doctor = Doctor(username=username,email=email)
            new_doctor.set_password(password)
            db.session.add(new_doctor)
            db.session.commit()
            flash('Doctor registered successfully.')
            return redirect(url_for('login'))
    return render_template('register.html')

def add_doctor(username, password,email ,is_admin):
    existing_doctor = Doctor.query.filter_by(username=username).first()
    if existing_doctor is None:
        new_doctor =  Doctor(username=username,email=email,is_admin=is_admin)
        new_doctor.set_password(password)
        db.session.add(new_doctor)
        db.session.commit()
        print(f'Added new doctor: {username}')
    else:
        print(f'Doctor with username {username} already exists.')


@app.route('/add_patient', methods=['GET', 'POST'])
@login_required
def add_patient():
    conditions = [
        "allergy", "block nose", "cold", "coughing", "diarrhea",
        "fever", "flu", "headache", "inflammation", "itchy",
        "muscle cramp", "phlegm", "pus", "rashes", "sneezing",
        "sore throat", "stomachache", "swollen sprain", "vomiting"
    ]
    conditions.sort()
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        condition = request.form.get('condition')
        description = request.form.get('description')
        doctor_id = current_user.id

        new_patient = Patient(
            name=name,
            age=age,
            gender=gender,
            condition=condition,
            description=description,
            doctor_id=doctor_id
        )
        db.session.add(new_patient)
        db.session.commit()
        flash('New patient added successfully.')
        return redirect(url_for('case'))

    return render_template('add_patient.html', conditions=conditions)

with app.app_context():
    db.create_all()
    add_doctor('yaoming', '1234','1304448069@qq.com',True)
    add_doctor('sixu', '4321', '2412705414@qq.com', True)
    #add_doctor('yang', '9876', '', False)  #put your email for 2FA here