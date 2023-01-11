import requests
from test_file1 import url1

if __name__ != "__main__":
    perf_errors = []


    def test_performance1(say_hi):
        response = requests.get(url1)
        assert response.elapsed.total_seconds() < 1, \
            perf_errors.append(f'Time is {response.elapsed.total_seconds()}')


    def test_performance2():
        post_this = {'title': 'cats', 'body': 'manul'}
        i = 0
        while i < 20:
            resp = requests.post(url1, json=post_this)
            i += 1
        assert resp.elapsed.total_seconds() < 10


