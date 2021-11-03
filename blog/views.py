
from django.urls import reverse_lazy
from django.utils.text import slugify

from blog.models import Books
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from blog.forms.Book_form import BookForm, BookCreateForm
from blog.mixins import RedirectToSuccesUrlMixIn


class BookView(ListView):
    queryset = Books.objects.all().order_by('title')
    template_name = 'main_page.html'
    context_object_name = 'Books'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'Book'


class EditBookDetail(RedirectToSuccesUrlMixIn, UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'EditBook.html'
    slug_url_kwarg = 'slug'


class CreateBook(CreateView):
    model = Books
    template_name = 'create_book.html'
    success_url = reverse_lazy('BookList')
    form_class = BookCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBook, self).form_valid(form)


class DeleteBook(RedirectToSuccesUrlMixIn, DeleteView):
    model = Books
    success_url = reverse_lazy('BookList')
    template_name = 'books_confirm_delete.html'
