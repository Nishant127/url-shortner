from rest_framework.exceptions import APIException
from .constants import URL_DOES_NOT_EXIST


class URL_DOES_NOT_EXIST_EXCEPTION(APIException):
    status_code = 400
    default_detail = URL_DOES_NOT_EXIST
