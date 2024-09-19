from django.db import connection

import string
import random

from core.models.url import Url


class Shortener:
    CHARSET = string.ascii_letters + string.digits
    SHORT_LEN = 6

    @staticmethod
    def __get_from_long(long_url: str) -> Url | None:
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT long_url, short_url FROM url WHERE long_url="{long_url}"')
            record = cursor.fetchone()
        return None if record is None else Url(record[0], record[1])

    @staticmethod
    def __create(long_url: str) -> Url:
        short_url = Shortener.__shorten_url()
        with connection.cursor() as cursor:
            cursor.execute(f'INSERT INTO url (long_url, short_url) VALUES ("{long_url}", "{short_url}")')
        return Url(long_url, short_url)

    @staticmethod
    def get_from_short(short_url: str) -> Url:
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT long_url, short_url FROM url WHERE short_url="{short_url}"')
            record = cursor.fetchone()
        return None if record is None else Url(record[0], record[1])

    @staticmethod
    def get_or_create(long_url: str) -> Url:
        record = Shortener.__get_from_long(long_url)
        if record is None:
            record = Shortener.__create(long_url)
        return record

    @staticmethod
    def __shorten_url() -> str:
        return ''.join(random.choice(Shortener.CHARSET) for _ in range(Shortener.SHORT_LEN))