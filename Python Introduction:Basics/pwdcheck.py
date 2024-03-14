import re 

def check_password(password):
    pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    a = pattern.match(password)
    if a is None:
        return 'Failed'
    else:
        return 'Works'

while True:
    arg1 = input("Enter a password: ")
    result = check_password(arg1)
    print(result)
    if result == 'Works':
        break