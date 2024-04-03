import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    response = None

    @allure.step("Get all memes")
    def get_all_memes(self, get_token=None):
        headers = {"Authorization": get_token}
        print(f'{self.url}/meme')
        self.response = requests.get(url=f'{self.url}/meme', headers=headers)
