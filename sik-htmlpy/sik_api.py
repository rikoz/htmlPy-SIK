import requests


ROOT_URL = 'http://localhost:8000'


def get_test(password):
    return requests.get(ROOT_URL+'/tests/'+password).json()


def get_profile(mat_number):
    return requests.get(ROOT_URL+'/students/'+mat_number).json()


def auth_user(mat_number, password):
    test = requests.get(ROOT_URL+'/tests/'+password)
    profile = requests.get(ROOT_URL+'/students/'+mat_number)

    if test.status_code == 200 and profile.status_code == 200:
        return True
    else:
        return False