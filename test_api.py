import json
import requests
from assertpy import assert_that
import pytest

url_0 = "https://www.aqa.science/"

response = requests.get(url_0).json()
print(type(response))

login = "admin"
pwd = "admin123"

#fixture needed to get data through the tests
@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}

#first test to get response from aqa.science and ensure that needed keys are presented in response
def test_get(change_data):
    response = requests.get(url_0)
    assert response.text == '{"users":"https://www.aqa.science/users/",' \
                            '"groups":"https://www.aqa.science/groups/"}'

    data = response.json()
    assert_that(data).contains_key("users", "groups")
    #this way we save dict to change data and can use it in next tests
    change_data.update(data)


#test to get response from users and ensure that response contains expected keys
def test_get_users(change_data):
    user_link = change_data["users"]
    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(user_link, auth=(login, pwd)).json()
    #this way ensure that expected keys are presented in response
    # * is needed to unpack list
    assert_that(response).contains_key(*expected_keys)

    print(response)


#this test needed to ensure that response from page contains expected keys
def test_get_users_2(change_data):
    next_url = "https://www.aqa.science/users/?page=2"

    expected_keys = ["count", "next", "previous", "results"]
    response = requests.get(next_url, auth=(login, pwd)).json()

    assert_that(response).contains_key(*expected_keys)

    with open("result.json", "w+") as f:
        json.dump(response, f)


#this test needed to ensure that user can be created
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


#this test needed to ensure that user data can be changed by PUT request
def test_put_users(change_data):
    put_data = {
            "username": "FGHJKL",
            "email": "kitkat@gmail.com",
            "groups": []
    }
    user_link = change_data["created_user_url"]
    response = requests.put(user_link, put_data, auth=(login, pwd)).json()
    assert_that(response).contains_value("kitkat@gmail.com")


#this test needed to ensure that user can be deleted
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
