import os
from time import sleep

from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django  # noqa

django.setup()

from apps.posts.models.post import Post


POSTS = [
    {'title': 'A', 'content': 'Foo'},
    {'title': 'B', 'content': 'Bar'},
    {'title': 'C', 'content': 'Blah'},
]


def posts(data: list):
    with transaction.atomic():
        for kwargs in data:
            Post.objects.create(**kwargs)  # noqa
            sleep(1)


if __name__ == '__main__':
    posts(data=POSTS)
