"""Module which contains controllers for book displaying """
from django.urls import reverse_lazy
from blog.models import Books
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from blog.forms.Book_form import BookForm, BookCreateForm
from blog.mixins import RedirectToSuccesUrlMixIn


class BookView(ListView):
    """"View for displaying the list of books"""
    queryset = Books.objects.all().order_by('title')
    template_name = 'main_page.html'
    context_object_name = 'Books'


class BookDetailView(DetailView):
    """"View for displaying the details of a specific book"""
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'Book'


class EditBookDetail(RedirectToSuccesUrlMixIn, UpdateView):
    """"View to edit the details of a specific book"""
    model = Books
    form_class = BookForm
    template_name = 'EditBook.html'
    slug_url_kwarg = 'slug'


class CreateBook(CreateView):
    """"View to create new book"""
    model = Books
    template_name = 'create_book.html'
    success_url = reverse_lazy('BookList')
    form_class = BookCreateForm

    def form_valid(self, form):
        """Append in parent class function ability to automatically identify the user"""
        form.instance.user = self.request.user
        return super(CreateBook, self).form_valid(form)


class DeleteBook(RedirectToSuccesUrlMixIn, DeleteView):
    """View to delete specific book"""
    model = Books
    success_url = reverse_lazy('BookList')
    template_name = 'books_confirm_delete.html'
