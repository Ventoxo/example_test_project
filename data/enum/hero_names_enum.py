from enum import Enum


class HeroNamesOneWord(Enum):
    AVALANCHE = "Avalanche"
    ABYSS = "Abyss"


class HeroNamesSeveralWords(Enum):
    ABSORBING_MAN = "Absorbing Man"
    ABYSS_AGE_OF_APOCALYPSE = "Abyss (Age of Apocalypse)"


class IncorrectHeroName(Enum):
    INCORRECT_NAME = "123123123123123123123123"
