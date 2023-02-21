from django.urls import path
from . import views

urlpatterns = [
    path("", views.CloneView.as_view()),
]