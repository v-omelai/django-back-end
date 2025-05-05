from django.contrib import admin


class TimestampAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )
