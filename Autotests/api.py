import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):
        headers = {'email': email, 'password': password}
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_pets_list(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/wallhaven-d66x7o.png')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type, 'accept': 'application/json'}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result



    def update_pet_info(self, auth_key, pet_id, name, animal_type, age, pet_photo):

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/wallhaven-d66x7o.png')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type, 'accept': 'application/json'}
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def delete_pet(self, auth_key, pet_id):

        headers = {'auth_key': auth_key['key'], 'accept': 'application/json'}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result