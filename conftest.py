import requests
import pytest
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import GetMeme
from endpoints.add_new_meme import AddNewMeme
from endpoints.update_meme_by_id import UpdateMeme
from endpoints.delete_meme_by_id import DeleteMeme


url = "http://167.172.172.115:52355"


@pytest.fixture()
def authorize_user():
    def _authorize_user(user_name):

        if check_token_freshness(user_name) == 401:
            data = {"name": user_name}
            response = requests.post(url=f'{url}/authorize', json=data)
            token = response.json()['token']
            return token
        else:
            return user_name

    return _authorize_user


@pytest.fixture()
def meme_id(authorize_user):
    new_meme = {
        "text":"deutsches_meme",
        "url": "https://www.web-netz.de/wp-content/uploads/730x330_website_header-18.jpg",
        "tags": ["german", "dog"],
        "info": {"colors":["white", "purple"]}
    }
    user_name = authorize_user('Vladimir')
    headers = {"Authorization": user_name}
    response = requests.post(url=f'{url}/meme', json=new_meme, headers=headers)
    meme_id = response.json()["id"]
    yield meme_id
    requests.delete(url=f'{url}/meme/{meme_id}', headers=headers)


def check_token_freshness(user_name):
    headers = {"Authorization": user_name}
    response = requests.get(url=f'{url}/meme', headers=headers)
    return response.status_code


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
