from urllib import request

from django.forms import ModelForm, Textarea

from blog.models import Books


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['review', 'title', 'page_count', 'publication', 'image', 'author']


class BookCreateForm(ModelForm):

    class Meta:
        model = Books
        exclude = ('slug', 'user')
