import requests
from django.conf import settings
from django.core.cache import cache
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.proxy.serializers import ProxySerializer
from apps.proxy.throttles import ProxyThrottle


class Proxy:
    @staticmethod
    def get(link: str, key: str) -> Response:
        cached = cache.get(key)

        if cached:
            response = Response(cached)
            response['X-Cache'] = 'HIT'
            return response

        response = requests.get(link)

        try:
            data = response.json()
        except Exception as e:
            data = {'error': f'Something went wrong: {e}'}

        if response.status_code != 200:
            return Response(data, status=response.status_code)

        cache.set(key, data, timeout=30)

        return Response(data)


@extend_schema_view(get=extend_schema(tags=['proxy'], operation_id='proxy_list', parameters=[
    OpenApiParameter(name='userId', type=int, required=False, description='Filter posts by userId'),
    OpenApiParameter(name='title', type=str, required=False, description='Filter posts by title'),
    OpenApiParameter(name='body', type=str, required=False, description='Filter posts by body'),
]))
class ProxyListView(generics.GenericAPIView):
    serializer_class = ProxySerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_classes = [ProxyThrottle]

    def get(self, request, *args, **kwargs):  # noqa
        params = request.query_params
        link = f'{settings.EXTERNAL_API_BASE}/posts'
        key = f'proxy_posts_{params.urlencode()}'
        return Proxy.get(link=link, key=key)


@extend_schema_view(get=extend_schema(tags=['proxy'], operation_id='proxy_retrieve'))
class ProxyRetrieveView(generics.GenericAPIView):
    serializer_class = ProxySerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_classes = [ProxyThrottle]

    def get(self, request, pk, *args, **kwargs):  # noqa
        link = f'{settings.EXTERNAL_API_BASE}/posts/{pk}'
        key = f'proxy_post_{pk}'
        return Proxy.get(link=link, key=key)
