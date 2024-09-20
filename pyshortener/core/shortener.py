from django.db import connection

import string
import random
import time

from core.models.url import Url


class Shortener:
    CHARSET = string.ascii_letters + string.digits
    # TODO move to settings
    SHORT_LEN = 6
    EXPIRATION_SECONDS = 365 * 24 * 60 * 60

    @staticmethod
    def __get_from_long(long_url: str) -> Url | None:
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT long_url, short_url, click_count FROM url WHERE long_url=%s',
                (long_url,)
            )
            record = cursor.fetchone()
        return None if record is None else Url(record[0], record[1], record[2])

    @staticmethod
    def __create(long_url: str) -> Url:
        short_url = Shortener.__shorten_url()
        expiration_timestamp = int(time.time()) + Shortener.EXPIRATION_SECONDS
        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO url (long_url, short_url, expiration_date) VALUES (%s, %s, %s)',
                (long_url, short_url, expiration_timestamp)
            )
        return Url(long_url, short_url, 0)

    @staticmethod
    def __shorten_url() -> str:
        return ''.join(random.choice(Shortener.CHARSET) for _ in range(Shortener.SHORT_LEN))

    @staticmethod
    def __increment_count(short_url: str) -> None:
        with connection.cursor() as cursor:
            cursor.execute(
                'UPDATE url SET click_count = click_count + 1 WHERE short_url=%s',
                (short_url,)
            )

    @staticmethod
    def get_from_short(short_url: str) -> Url | None:
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT long_url, short_url, click_count FROM url WHERE short_url=%s',
                (short_url,)
            )
            record = cursor.fetchone()
        if record:
            Shortener.__increment_count(short_url)
            return Url(record[0], record[1], record[2])

    @staticmethod
    def get_or_create(long_url: str) -> Url:
        record = Shortener.__get_from_long(long_url)
        if record is None:
            record = Shortener.__create(long_url)
        return record