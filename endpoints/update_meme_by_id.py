import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step("Update meme by id")
    def update_meme_by_id(self, body, user, id):
        headers = {"Authorization": user}
        self.response = requests.put(url=f'{self.url}/meme/{id}', json=body, headers=headers)
