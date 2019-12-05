from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):

    """ Banner Admin Definition """

    list_display = ("get_thumbnail", "name")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70%" src="{obj.image.url}" />')

    get_thumbnail.short_description = "배너"
