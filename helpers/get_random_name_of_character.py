import enum
import random


class GetRandomCharacterName:

    @staticmethod
    def get_random_name_of_character(hero_names_dir: enum.EnumMeta) -> str:
        list_of_names = []
        for attribute in dir(hero_names_dir):
            if attribute[0] != '_':
                list_of_names.append(getattr(hero_names_dir, attribute))
        random_name = random.choice(list_of_names)
        return random_name.value
