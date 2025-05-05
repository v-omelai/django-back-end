from django.contrib import admin

from apps.core.admin import TimestampAdmin
from apps.posts.models.post import Post


admin.site.register(Post, TimestampAdmin)
