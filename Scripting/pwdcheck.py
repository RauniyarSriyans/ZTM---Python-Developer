import requests
import hashlib
import sys

# hash is indempotent --> meaning same output for same input always)

def request_api_data(query_char):
    # url + first 5 chars in the sha1 hash of password
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # get the response back from the API
    res = requests.get(url)
    # check if response was OK
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    # return whatever response you got
    return res

def get_password_leaks_count(api_response, hash_to_check):
    # 
    hashes = (line.split(':') for line in api_response.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # get password from the user, then hash the password using sha1 and then do hexdigest to get the string representation of the hash
    hashed_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # because the API takes first 5 chars, and returns the list of remaining chars and count, split it
    first5_char, remaining = hashed_pw[:5], hashed_pw[5:]
    # make the API call
    api_response = request_api_data(first5_char)
    # call another function to get the actual count for this password
    return get_password_leaks_count(api_response, remaining)
    
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times ... you should change your password')
        else:
            print(f'{password} is safe, carry on!')
    return 'done'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))