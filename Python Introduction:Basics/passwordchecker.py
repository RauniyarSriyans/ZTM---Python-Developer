username = input("What is your username? \n")
password = input("Enter your password: \n")
placeholder = '*' * len(password)
print(f'Hey {username}, your password {placeholder} is {len(password)} characters long.')