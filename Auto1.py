import requests


def login_check(url, user_login_data):
    return requests.post(url, json=user_login_data).json()


def get_apps(url, prms):
    return requests.get(url, headers=prms).json()


a = "https://dev-k8s-api.ecto.com/api/user/profile"
b = "https://dev-k8s-api.ecto.com/api/login_check"

user_login_data = {"username": "77yan",
                   "password": "Fishfish&"
                   }
params = {"authorization": "Bearer " + (login_check(b, user_login_data)['token'])}

print(login_check(b, user_login_data)['token'])
print(get_apps(a, params)['applications'])

