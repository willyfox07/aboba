from django.contrib import admin
from blog.models import  Language, Books, Video


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Class for configure panel of admin"""
    pass


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    """Class for configure panel of admin"""
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Class for configure panel of admin"""
    pass


