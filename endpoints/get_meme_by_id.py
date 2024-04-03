import requests
import allure
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.step("Get meme by id")
    def get_meme_by_id(self, get_token, id):
        headers = {"Authorization": get_token}
        self.response = requests.get(url=f'{self.url}/meme/{id}', headers=headers)
