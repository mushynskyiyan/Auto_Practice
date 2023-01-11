import pytest


@pytest.fixture
def say_hi():
    print("Here we go")


@pytest.fixture
def save_data():
    with open("data.log", "w+") as f:
        f.write("Data for tests")


