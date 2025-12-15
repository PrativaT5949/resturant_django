from django.urls import path
from . import views
from .views import Contact_view, success_view

urlpatterns = [
    path("", Contact_view, name="contact"),
    path("contact/success/", success_view, name="success"),
]
