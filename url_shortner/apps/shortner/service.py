from string import ascii_letters, digits
from django.conf import settings
from random import choice
from .models import Shortner
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import URL_DOES_NOT_EXIST_EXCEPTION


class ShortnerService:
    @classmethod
    def generate_random_code(cls):
        ALL_POSSIBLE_CHARACTERS = ascii_letters + digits
        code = "".join(
            choice(ALL_POSSIBLE_CHARACTERS) for i in range(settings.SHORT_URL_CODE_LEN)
        )
        return code

    @classmethod
    def get_unique_short_url_code(cls):
        short_url_code = cls.generate_random_code()
        if Shortner.objects.filter(short_url=short_url_code).exists():
            return cls.generate_random_code()
        return short_url_code

    @classmethod
    def save_short_url(cls, original_url):
        short_url_code = cls.get_unique_short_url_code()
        Shortner.objects.create(original_url=original_url, short_url=short_url_code)
        return short_url_code

    @classmethod
    def get_original_url(cls, short_url_code):
        try:
            short_url = Shortner.objects.get(short_url=short_url_code, is_active=True)
            return short_url.original_url
        except ObjectDoesNotExist as e:
            raise URL_DOES_NOT_EXIST_EXCEPTION
