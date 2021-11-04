"""Module with Book forms"""
from django.forms import ModelForm
from blog.models import Books


class BookForm(ModelForm):
    """Class for creating a form for editing a book """
    class Meta:
        """Class which selected fields from book-model for form"""
        model = Books
        fields = ['review', 'title', 'page_count', 'publication', 'image', 'author']


class BookCreateForm(ModelForm):
    """Class for creating a form for creating a book """
    class Meta:
        """Class which selected fields from book-model for form"""
        model = Books
        exclude = ('slug', 'user')
