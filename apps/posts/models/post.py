from django.db import models

from apps.core.models.timestamp import Timestamp


class Post(Timestamp):
    class Meta:
        ordering = ['-created_at']

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
