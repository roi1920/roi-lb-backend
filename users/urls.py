from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("<int:pk>", views.UsersModifyView.as_view()),
    path("admin/<int:pk>", views.UserAdminToggle.as_view())
]
