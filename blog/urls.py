from django.urls import path, include
from blog.views import BookView, BookDetailView, EditBookDetail, DeleteBook, CreateBook

urlpatterns = [
    path('', BookView.as_view(), name='BookList'),
    path('<slug:slug>', BookDetailView.as_view(), name='BookDetail'),
    path('<slug:slug>/edit', EditBookDetail.as_view(), name='EditBook'),
    path('<slug:slug>/delete', DeleteBook.as_view(), name='DeleteBook'),
    path('create/', CreateBook.as_view(), name='CreateBook'),
]