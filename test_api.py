import json
import requests
from assertpy import assert_that
import pytest

url_0 = "https://www.aqa.science/"

response = requests.get(url_0).json()
print(type(response))

login = "admin"
pwd = "admin123"


@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}


def test_get(change_data):
    response = requests.get(url_0)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'

    data = response.json()
    assert_that(data).contains_key("users", "groups")
    change_data.update(data)


def test_get_users(change_data):
    user_link = change_data["users"]
    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(user_link, auth=(login, pwd)).json()

    assert_that(response).contains_key(*expected_keys)

    print(response)


def test_get_users_2(change_data):
    next_url = "https://www.aqa.science/users/?page=2"

    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(next_url, auth=(login, pwd)).json()

    assert_that(response).contains_key(*expected_keys)

    with open("result.json", "w+") as f:
        json.dump(response, f)


def test_post_users(change_data):
    post_data = {
            "username": "FGHJKL",
            "email": "dddddd@ggggggk.com",
            "groups": []
    }
    expected_keys = ["username", "email", "groups"]
    user_link = change_data["users"]
    response = requests.post(user_link, post_data, auth=(login, pwd)).json()
    created_user_url = response['url']
    change_data["created_user_url"] = created_user_url
    assert_that(response).contains_key(*expected_keys)

    with open("result.json", "w+") as f:
        json.dump(response, f)


def test_put_users(change_data):
    put_data = {
            "username": "FGHJKL",
            "email": "kitkat@gmail.com",
            "groups": []
    }
    user_link = change_data["created_user_url"]
    response = requests.put(user_link, put_data, auth=(login, pwd)).json()
    assert_that(response).contains_value("kitkat@gmail.com")


def test_delete_users(change_data):
    user_link = change_data["created_user_url"]
    response = requests.delete(user_link, auth=(login, pwd))
    print(response.text)


def test_post_users2(change_data):
    post_data = {
        "username": "FisherJack22",
        "email": "fishers22@jack.com",
        "groups": []
    }
    expected_values = ["FisherJack22", "fishers22@jack.com"]
    user_link = change_data["users"]
    response = requests.post(user_link, post_data, auth=(login, pwd)).json()
    created_user_url = response['url']
    change_data["created_new_user_url"] = created_user_url
    assert_that(response).contains_value(*expected_values)


def test_delete_users2(change_data):
    user_link = change_data["created_new_user_url"]
    response = requests.delete(user_link, auth=(login, pwd))
    print(response)
