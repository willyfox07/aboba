from django.contrib import admin
from django.utils.text import slugify

from blog.models import  Language, Books, Video


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


