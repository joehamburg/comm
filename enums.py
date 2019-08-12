from enum import Enum


class _CHARACTER(Enum):
    HUNTER = 1
    PIRATE = 2
    NINJA = 3
    HERO = 4

class Container(Enum):
    UNKNOWN = 1
    CHARACTER = _CHARACTER

