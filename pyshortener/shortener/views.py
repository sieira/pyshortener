import logging

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.shortener import Shortener

LOGGER = logging.getLogger(__name__)


@api_view(['POST'])
def shorten(request):
    url = request.data.get('url', '')
    validator = URLValidator()

    try:
        validator(url)
    except ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    shortened_url = Shortener.get_or_create(url).short_url
    # TODO get it form settings or request
    own_host = 'localhost:8080'
    return Response(data=f'{own_host}/{shortened_url}', status=status.HTTP_200_OK)