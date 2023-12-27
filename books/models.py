from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=120)
    available_copies = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now(), blank=True)
    img_url = models.CharField(max_length=255)
    borrowers = models.ManyToManyField(User, through='Borrow')

    def serialize(book):
        return {
            "id": book.pk,
            'title': book.title,
            'available_copies': book.available_copies,
            'date_added': book.date_added,
            'img_url': book.img_url,
        }

    def serialize_lst(books):
        return [
            {
                "id": book.pk,
                'title': book.title,
                'available_copies': book.available_copies,
                'date_added': book.date_added,
                'img_url': book.img_url,
            } for book in books
        ]


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
