from assertpy import assert_that
import allure

from helpers.get_random_name_of_character import GetRandomCharacterName
from data.enum.errors_enum import Errors
from data.enum.hero_names_enum import HeroNamesOneWord, HeroNamesSeveralWords, IncorrectHeroName


class TestGetCharByName:

    # @allure.id("id")
    # @allure.story("GetCharacterByName")
    # @allure.suite("Smoke tests")
    # @allure.title("Получаем персонажа по одному слову (по имени)")
    # @allure.tag("positive")
    def test_get_character_by_single_word(self, test_client):
        name = GetRandomCharacterName.get_random_name_of_character(HeroNamesOneWord)
        self._get_and_check_character(name=name, test_client=test_client)

    # @allure.id("id")
    # @allure.story("GetCharacterByName")
    # @allure.suite("Smoke tests")
    # @allure.title("Получаем персонажа по нескольким словам (по имени)")
    # @allure.tag("positive")
    def test_get_character_by_several_words(self, test_client):
        name = GetRandomCharacterName.get_random_name_of_character(HeroNamesSeveralWords)
        self._get_and_check_character(name=name, test_client=test_client)

    # @allure.id("id")
    # @allure.story("GetCharacterByName")
    # @allure.suite("Smoke tests")
    # @allure.title("Получаем персонажа по неправильному имени")
    # @allure.tag("negative")
    def test_get_character_by_incorrect_name(self, test_client):
        name = IncorrectHeroName.INCORRECT_NAME.value
        character_by_name_response = test_client.get_one_character(name).json()
        actual_response = character_by_name_response["error"].lower()

        assert_that(
            actual_response,
            f"Получено {character_by_name_response} вместо сообщения об ошибке"
        ).is_equal_to(Errors.INCORRECT_NAME_ERROR.value)

    @staticmethod
    def _get_and_check_character(name, test_client):
        # with allure.step("Получить персонажа"):
        character_by_name_response = test_client.get_one_character(name).json()
        actual_response = character_by_name_response["result"]["name"]

        # with allure.step("Проверить, что имя, полученной по апи, совпадает с изначальным именем"):
        assert_that(
            actual_response,
            f"Неправильное имя у персонажа, должно быть {name}, а получено {actual_response}"
        ).is_equal_to(name)
