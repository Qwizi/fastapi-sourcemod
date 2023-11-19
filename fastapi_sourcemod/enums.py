
from enum import Enum


class AuthTypeEnum(str, Enum):
    STEAM = "steam"
    NAME = "name"
    IP = "ip"