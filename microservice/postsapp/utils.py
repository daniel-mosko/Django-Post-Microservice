import requests


def valid_user(uid):
    res = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for post in range(len(res)):
        if uid == res[post]['id']:
            return True
    return False


def fetch_post(id):
    res = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    for post in range(len(res)):
        if id == res[post]['id']:
            return res[post]
