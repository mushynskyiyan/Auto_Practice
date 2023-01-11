import requests
url1 = "https://jsonplaceholder.typicode.com/posts"

errors = []


def append_data(data):
    with open("data.log", "a") as f:
        f.write(f"{data}")


def test_one(save_data):
    response = requests.get(url1)
    stat_code = response.status_code
    assert stat_code == 200, errors.append(stat_code)


def test_two():
    response = requests.get(url1)
    data_test = response.text
    assert len(data_test) > 0, errors.append("Data is empty")
    append_data(data_test)


def test_three():
    post_this = {'title': 'cats', 'body': 'manul'}
    response = requests.post(url1, json=post_this)
    code = response.status_code
    data_for_test = response.text
    print(data_for_test)
    assert code == 201, errors.append(code)
    append_data(data_for_test)


def test_four():
    patch_this = {
    "title": "let it be",
    "body": "go go go"
  }
    response = requests.patch(f'{url1}/1', json=patch_this)
    data_text = response.text
    assert "let it be" in data_text, errors.append("Patch request failed")
    append_data(data_text)




