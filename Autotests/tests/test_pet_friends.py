import os
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

"""ПОЗИТИВНЫЕ ТЕСТЫ"""

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_pets_list_wiyh_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pets_list(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet(name = 'Bob', animal_type = 'Dog', age = '3', pet_photo = 'images/wallhaven-d66x7o.png'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    print(result['id'])


def test_change_new_pet(pet_id = '131b2a4b-ff41-49ec-a8ae-05c79a9764af', name = 'Rick', animal_type = 'Dog', age = '3', pet_photo = 'images/wallhaven-d66x7o.png'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_delete_pet(pet_id = '131b2a4b-ff41-49ec-a8ae-05c79a9764af'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

"""НЕГАТИВНЫЕ ТЕСТЫ"""

def test_get_api_key_for_invalid_user(email = 'invalid', password = 'invalid'):
    status, result = pf.get_api_key(email, password)
    assert status == 200
