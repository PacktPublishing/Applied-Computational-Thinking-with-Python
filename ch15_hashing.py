import uuid
import hashlib

def hash_pwd(password):
    salt = uuid.uuid4().hex 
    return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_pwd(hashed_pwd, user_pwd):
    password, salt = hashed_pwd.split(':')
    return password == hashlib.sha1(salt.encode() + user_pwd.encode()).hexdigest()

new_pwd = input('Enter new password: ')
hashed_pwd = hash_pwd(new_pwd)
print('Hashed password: ' + hashed_pwd)
confirm_pwd = input('Confirm password: ')

if check_pwd(hashed_pwd, confirm_pwd):
    print('Confirmed!')
else:
    print('Please try again')
