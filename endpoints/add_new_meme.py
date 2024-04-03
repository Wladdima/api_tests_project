import requests
import allure
from endpoints.endpoint import Endpoint


class AddNewMeme(Endpoint):

    @allure.step("Add new meme")
    def add_new_meme(self, get_token, body):
        headers = {"Authorization": get_token}
        self.response = requests.post(url=f'{self.url}/meme', json=body, headers=headers)
