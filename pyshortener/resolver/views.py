from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core.shortener import Shortener


@api_view(['GET'])
def resolve(request: Request, short_url: str) -> Response:
    url = Shortener.get_from_short(short_url)
    if url is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 307 specifies that the method should not change, allowing to POST from the browser through the redirection
    return Response(status=status.HTTP_307_TEMPORARY_REDIRECT, data=url.long_url)