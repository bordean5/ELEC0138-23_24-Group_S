# ELEC0138 Security and Privacy 23/24 Group_S

## Description
This project simulates an Electronic Health Record (EHR) System which allows hospital staff to upload and search patients' electronic records. Based on the threat model, this project designs and simulates a number of cyber-attacks against the base version of the EHR system with poor security design. A secure website system with techniques to defend against these attacks is built.

### Four attacks are simulated which could hack the web with bad design:  
1. Phishing email and website
2. SQL injection attack
3. Brute force attack
4. Dos attack (HTTP flooding)

### To defend against these attacks, our website has implemented security designs:
1. Two-factor authentication (2FA)
2. Rate-limiting feature (IP banning)
3. limits of authority
4. Security Headers
5. Parametrized queries

## Program structure
-- ELEC0138 Security and Privacy 23/24 Group_S
```
- EHR website base version
- EHR website secure version
- Phishing website
- requirements.txt
- README.md
```
- `EHR website base version/`: The base version of the EHR website allows SQL injection, brute force and DOS attack
- `EHR website secure version/`: The secure version of the EHR website with a better secure design and better user interface
- `Phishing website/`: Send the target phishing email with like to the phishing website which steals user passwords
- `requirements.txt`: Contains Python environment dependencies
- `README.md`:The README file for the project.

## Program run instruction
1. Clone the repository
2. Create a new Python env with version 3.9 and install the dependencies with requirement.txt
3. Open each folder to run the corresponding part
4. The instructions for each part are detailed in the readme file within each folder
 

