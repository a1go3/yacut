import string
from random import choices

from .models import URLMap


def get_unique_short_id():
    """Функция для генерации короткой ссылки. """
    while True:
        short_link = ''.join(
            choices(string.digits + string.ascii_letters, k=6))
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link
