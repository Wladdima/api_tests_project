import requests
import pytest
import os

from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import GetMeme
from endpoints.add_new_meme import AddNewMeme
from endpoints.update_meme_by_id import UpdateMeme
from endpoints.delete_meme_by_id import DeleteMeme


url = "http://167.172.172.115:52355"


@pytest.fixture(scope='session')
def get_token():

    if not os.path.exists("token.txt"):
        with open("token.txt", 'w'): pass

    with open("token.txt", "r") as token_file:
        token = token_file.read()

    if check_token_freshness(token) == 404:
        data = {"name": "Vladimir"}
        response = requests.post(url=f'{url}/authorize', json=data)
        token = response.json()['token']
    
        with open("token.txt", "w") as token_file:
            token_file.write(token)

    return token


def check_token_freshness(token):
    response = requests.get(url=f'{url}/authorize/{token}')
    return response.status_code


@pytest.fixture()
def meme_id(get_token):
    new_meme = {
        "text":"deutsches_meme",
        "url": "https://www.web-netz.de/wp-content/uploads/730x330_website_header-18.jpg",
        "tags": ["german", "dog"],
        "info": {"colors":["white", "purple"]}
    }
    headers = {"Authorization": get_token}
    response = requests.post(url=f'{url}/meme', json=new_meme, headers=headers)
    meme_id = response.json()["id"]
    yield meme_id
    requests.delete(url=f'{url}/meme/{meme_id}', headers=headers)


@pytest.fixture()
def get_all_memes_endpoint():
    return  GetAllMemes()


@pytest.fixture()
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def add_new_meme_endpoint():
    return AddNewMeme()

@pytest.fixture()
def update_meme_endpoint():
    return  UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
