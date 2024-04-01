import requests
import allure


class Endpoint():

    url = "http://167.172.172.115:52355"
    response = None


    @allure.step("Check response status code is 200")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is incorrect"


    @allure.step("Check response status code is 403")
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, "Status code is incorrect"


    @allure.step("Check response status code is 404")
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, "Status code is incorrect"
    

    @allure.step("Check response status code is 401")
    def check_status_code_is_401(self):
        assert self.response.status_code == 401, "Status code is incorrect"


    @allure.step("Check response status code is 400")
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, "Status code is incorrect"


    @allure.step("Check meme info")
    def check_meme_info(self, meme_info):
        assert meme_info == self.response.json()['info']


    @allure.step("Check meme tags")
    def check_meme_tags(self, meme_tags):
        assert meme_tags == self.response.json()['tags']


    @allure.step("Check meme text")
    def check_meme_text(self, meme_text):
        assert meme_text == self.response.json()['text']


    @allure.step("Check meme updated by meme")
    def check_meme_updated_by_name(self, user_name):
        assert user_name == self.response.json()['updated_by']
