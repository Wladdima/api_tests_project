import pytest
import allure


@allure.story("Memes")
@allure.feature("Get all memes")
@allure.title("Test get all memes")
@pytest.mark.positive
def test_get_all_memes(authorize_user, get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(user=authorize_user('Vladimir'))
    get_all_memes_endpoint.check_status_code_is_200()


@allure.story("Memes")
@allure.feature("Get one meme")
@allure.title("Test get one meme by id")
@pytest.mark.positive
def test_get_meme_by_id(authorize_user, get_meme_endpoint, meme_id):
    get_meme_endpoint.get_meme_by_id(id=meme_id, user=authorize_user('Vladimir'))
    get_meme_endpoint.check_status_code_is_200()


@allure.story("Memes")
@allure.feature("Add new meme")
@allure.title("Test add new meme")
@pytest.mark.positive
def test_add_new_meme(authorize_user, add_new_meme_endpoint):
    new_meme = {
        "text":"deutsches_meme",
        "url": "https://www.web-netz.de/wp-content/uploads/730x330_website_header-18.jpg",
        "tags": ["german", "dog"],
        "info": {"colors":["white", "purple"]}
    }
    add_new_meme_endpoint.add_new_meme(user=authorize_user('Vladimir'), body=new_meme)
    add_new_meme_endpoint.check_status_code_is_200()
    add_new_meme_endpoint.check_meme_info(new_meme["info"])
    add_new_meme_endpoint.check_meme_text(new_meme["text"])
    add_new_meme_endpoint.check_meme_tags(new_meme["tags"])
    add_new_meme_endpoint.check_meme_updated_by_name('Vladimir')


@allure.story("Memes")
@allure.feature("Update meme")
@allure.title("Test update meme by id")
@pytest.mark.positive
def test_update_meme(authorize_user, update_meme_endpoint, meme_id):
    updated_meme = {
        "id": meme_id,
        "text": "deutsches_memes",
        "url": "https://cdni-pageflow.wdr.de/main/image_files/processed_attachments/000/029/194/v3/medium/memes_harmlos_mobil.JPG",
        "tags": ["german", "girl", "instagram"],
        "info": {"colors": ["blue", "white"]}
    }
    update_meme_endpoint.update_meme_by_id(user=authorize_user('Vladimir'), body=updated_meme, id=meme_id)
    update_meme_endpoint.check_status_code_is_200()


@allure.story("Memes")
@allure.feature("Delete meme")
@allure.title("Test delete meme by id")
@pytest.mark.positive
def test_delete_meme(authorize_user, delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme_by_id(user=authorize_user('Vladimir'), id=meme_id)
    delete_meme_endpoint.check_status_code_is_200()
    delete_meme_endpoint.check_meme_deleted(user=authorize_user('Vladimir'), id=meme_id)
    delete_meme_endpoint.check_status_code_is_404()


@allure.story("Memes")
@allure.feature("Get meme")
@allure.title("Test get memes by id with unauthorized user")
@pytest.mark.negative
def test_get_meme_unauthorized_user(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(user="unauthorized user")
    get_all_memes_endpoint.check_status_code_is_401()


@allure.story("Memes")
@allure.feature("Get meme")
@allure.title("Test get meme with empty id")
@pytest.mark.negative
def test_get_meme_unauthorized_user(authorize_user, get_meme_endpoint):
    get_meme_endpoint.get_meme_by_id(user=authorize_user('Vladimir'), id='')
    get_meme_endpoint.check_status_code_is_404()


@allure.story("Memes")
@allure.feature("Get meme")
@allure.title("Test get meme by invalid id")
@pytest.mark.negative
def test_get_meme_invalid_id(authorize_user, get_meme_endpoint):
    get_meme_endpoint.get_meme_by_id(user=authorize_user('Vladimir'), id="abcde")
    get_meme_endpoint.check_status_code_is_404()


@allure.story("Memes")
@allure.feature("Add new meme")
@allure.title("Test add new meme without body")
@pytest.mark.negative
def test_add_meme_without_body(authorize_user, add_new_meme_endpoint):
    new_meme = {}
    add_new_meme_endpoint.add_new_meme(user=authorize_user('Vladimir'), body=new_meme)
    add_new_meme_endpoint.check_status_code_is_400()


@allure.story("Memes")
@allure.feature("Update meme")
@allure.title("Test update foreign meme")
@pytest.mark.negative
def test_update_foreign_meme(authorize_user, update_meme_endpoint):
    updated_meme = {
        "id": 1111,
        "text": "new_meme_text",
        "url": "https://cdni-pageflow.wdr.de/main/image_files/processed_attachments/000/029/194/v3/medium/memes_harmlos_mobil.JPG",
        "tags": ["new_tag_1", "updated_tag_2"],
        "info": {"objects": ["picture", "text"]}
    }
    update_meme_endpoint.update_meme_by_id(user=authorize_user('Vladimir'), body=updated_meme, id=1)
    update_meme_endpoint.check_status_code_is_403()


@allure.story("Memes")
@allure.feature("Delete meme")
@allure.title("Test delete foreign meme")
@pytest.mark.negative
def test_delete_foreign_meme(authorize_user, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_by_id(user=authorize_user('Vladimir'), id=1)
    delete_meme_endpoint.check_status_code_is_403()


@allure.story("Memes")
@allure.feature("Delete meme")
@allure.title("Test delete unexistable meme")
@pytest.mark.negative
def test_delete_unexistable_meme(authorize_user, delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme_by_id(user=authorize_user('Vladimir'), id=meme_id)
    delete_meme_endpoint.check_status_code_is_200()
    delete_meme_endpoint.check_meme_deleted(user=authorize_user('Vladimir'), id=meme_id)
    delete_meme_endpoint.delete_meme_by_id(user=authorize_user('Vladimir'), id=meme_id)
    delete_meme_endpoint.check_status_code_is_404()
