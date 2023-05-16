from string import ascii_letters, digits
from django.conf import settings
from random import choice


class ShortnerService:
    @classmethod
    def generate_random_code(cls):
        ALL_POSSIBLE_CHARACTERS = ascii_letters + digits
        code = "".join(
            choice(ALL_POSSIBLE_CHARACTERS) for i in range(settings.SHORT_URL_CODE_LEN)
        )
        return code
