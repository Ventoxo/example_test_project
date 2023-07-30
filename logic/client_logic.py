import requests
from requests.auth import HTTPBasicAuth
from data.enum.urls_enum import Urls


class ClientLogic:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.rest_api = self.authorize()
        self.rest_url = Urls.REST_IVI_URL.value

    def authorize(self):
        rest_api = requests.session()

        basic_auth = HTTPBasicAuth(self.username, self.password)
        rest_api.auth = basic_auth
        return rest_api

    def get_all_characters(self):
        response = self.rest_api.get(self.rest_url + "characters")
        return response

    def get_one_character(self, name):
        response = self.rest_api.get(self.rest_url + "character",
                                     params={"name": name}
                                     )
        return response

    def reset_table(self):
        response = self.rest_api.post(self.rest_url + "reset")
        return response

