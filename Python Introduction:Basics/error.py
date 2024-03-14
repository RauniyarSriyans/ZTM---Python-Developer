# error handling 

while True: 
    try:
        age = int(input('What is your age?'))
        print(f'your age is {age}')
        10 / age
        # err is a variable here that stores the error message
    except ValueError as err:
        print(f'received an error {err}')
    except ZeroDivisionError as err2:
        print(f'received an error {err2}')
    else:
        print('thank you!')
        break
    # this happens regardless of whether error is raised or not
    finally:
        print('ok, i am finally done')