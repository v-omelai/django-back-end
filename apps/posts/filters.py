from django_filters import FilterSet, CharFilter

from apps.posts.models.post import Post


class PostFilter(FilterSet):
    sort = CharFilter(method='filter_order')

    class Meta:
        model = Post
        fields = []

    def filter_order(self, queryset, name, value):
        order = self.request.query_params.get('order', 'desc')
        if value not in ['title', 'created_at']:
            return queryset
        prefix = '' if order == 'asc' else '-'
        return queryset.order_by(f'{prefix}{value}')
