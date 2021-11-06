"""Module which contain models for blog-application"""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from pytils.translit import slugify


class Books(models.Model):
    """CLass for creating book table in database"""
    title = models.CharField(max_length=30, verbose_name="Название")
    publication = models.DateField(verbose_name="Дата издания")
    page_count = models.IntegerField(max_length=5, verbose_name="Количество страниц")
    slug = models.SlugField()
    author = models.CharField(max_length=30,  verbose_name="Автор")
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Язык")
    image = models.ImageField(upload_to="img/", verbose_name='Обложка')
    review = models.TextField(max_length=1000, verbose_name='Рецензия', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    class Meta:
        """Function which contains configuration for parent class"""
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        """Function for string representation of a class"""
        return f'{self.author} - {self.title}'

    def save(self, *args, **kwargs):
        """Function to automatically create slug"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """ Function for autodetecting url of a class object """
        return reverse('BookDetail', kwargs={'slug': self.slug})




class Language(models.Model):
    """CLass for creating language table in database"""
    language = models.CharField(max_length=30, verbose_name="Язык")

    def __str__(self):
        """Function for string representation of a class"""
        return self.language


class Video(models.Model):
    """CLass for creating video table in database"""
    video_name = models.CharField(max_length=50, verbose_name="Название видео")
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        """Function for string representation of a class"""
        return self.video_name
