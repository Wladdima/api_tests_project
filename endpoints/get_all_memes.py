import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    response = None

    @allure.step("Get all memes")
    def get_all_memes(self, user):

        if user == "unauthorized user":
            self.response = requests.get(url=f'{self.url}/meme')
        else:
            headers = {"Authorization": user}
            self.response = requests.get(url=f'{self.url}/meme', headers=headers)
