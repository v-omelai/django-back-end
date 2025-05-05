from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from .filters import PostFilter
from .models.post import Post
from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100


@extend_schema_view(
    post=extend_schema(tags=['posts']),
    get=extend_schema(tags=['posts'], parameters=[
        OpenApiParameter(name='sort', description='title, created_at (default: created_at)', required=False, type=str),
        OpenApiParameter(name='order', description='asc or desc (default: desc)', required=False, type=str),
    ]),
)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  # noqa
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [AllowAny]
    authentication_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter


@extend_schema(tags=['posts'])
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  # noqa
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
