from django.test import TestCase
from blog.models import Books

class TestBooksModel(TestCase):

    def setUpTestData(cls) -> None:
        Books.objects.create(title='Мастер и Маргарита',
                             publication='1982-02-02',
                             page_count='682',
                             author='Булгаков',
                             language='1',
                             )
