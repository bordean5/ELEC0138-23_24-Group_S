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

Brute force:

To start the test, run the bruteforce.py file while using the pre-defined username or change it to the username you added in the app.py, 
to brute force the password. It will first search through the password in the dictionary.txt file and if none of them, 
it will try generating and testing passwords of increasing length from 1 to 4 digits, using only numeric characters. 
You can adjust the dictionary.txt file to test various passwords.

Dos:

To start the test, run the dos.py file to implement the dos attack.
It will send mountains of HTTP GET requests to the url by using "thread" to do this concurrently.
Adjust the number in "for i in range(50)" to use different number of threads to change the speed of request.
