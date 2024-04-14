# EHR website secure version

## Description
This folder implements a secure Electronic Health Record (EHR) system with techniques to defend against priority threats. Compared to the base version, it has many secure designs such as 2FA, rate limiting, and authority. Also, it has a better user interface and more functions.

### To defend against these attacks, our website has implemented security designs:
1. Two-factor authentication (2FA)
2. Rate-limiting feature (IP banning)
3. limits of authority
4. Security Headers
5. Parametrized queries

## Program structure
-- EHR website secure version
```
- instance
- template
- app.py
- two_factor_verification.py
- README.md
```
- `instance/`: Database file folder
- `template/`: Website HTML files
- `app.py`: main program 
- `two_factor_verification.py`: contains functions to generate 2FA code and send it to the target 
- `README.md`:The README file for the project.

## Program run instruction
1. Clone the repository
2. Complete the steps of the main readme file
3. Open this folder with the editor
4. Run the line "flask run" on the terminal to run the web server
5. Click the local link generated below: Running on http://127.0.0.1:5000
6. Create your own account in the last row of app.py with your name, password, email(2FA) and admin type (bool)
7. Generate the 2FA code with the button, get the code from account email and login

## Note
1. You have to create a new account as we do not know your email to send 2FA code
2. The 2FA last for 5 minutes and 3 tries. Or it expired
3. You can only request 2FA 3 times per minute
4. Only the admin account has the function to register a new user(not admin)
 

