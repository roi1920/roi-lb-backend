from django.urls import path
from . import views

urlpatterns = [
    path("", views.BooksView.as_view()),
    path("<int:pk>", views.BooksModifyView.as_view()),
    path("borrow/", views.BorrowBooks.as_view()),
    path("borrow/<int:pk>", views.BorrowBooks.as_view())
]
