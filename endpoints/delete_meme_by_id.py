import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step("Delete meme by id")
    def delete_meme_by_id(self, id, user):
        headers = {"Authorization": user}
        self.response = requests.delete(url=f'{self.url}/meme/{id}', headers=headers)


    @allure.step("Check meme deleted")
    def check_meme_deleted(self, user, id):
        headers = {"Authorization": user}
        self.response = requests.get(f"{self.url}/meme/{id}", headers=headers)
