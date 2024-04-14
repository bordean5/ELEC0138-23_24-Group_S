# Phishing email and website

## Description
In this attack, a phishing email is sent to the target doctor, using the reason that the system is stuck and needs to be updated to induce the doctor to click on the link and log into the (Electronic Health Records) EHR systems. In this case, the doctor's username and password will be recorded to complete the attack.

### Two main parts about phishing
1. phishing email
2. phishing website (app.py)

- `phishing_email.py`: Send phishing emails to targeted doctors with links to phishing website
- `app.py(phishing_website)`:A web page with a login interface similar to the basic version of the EHR web page, which saves the user name and password of the logged-in person to the password.txt file
- `README.md`:The README file for phishing.

## Program run instruction
1. Clone the repository
2. Complete the steps of the main readme file
3. Changing the recipient's email address in `phishing_email.py` can alter the recipient of the phishing email.
4. Run the line "flask run" on the terminal
5. Click the local link generated below: “Running on http://127.0.0.1:5000”
6. Enter username and password
7. The username and password used for logging in are saved in the file password.txt within the instance
