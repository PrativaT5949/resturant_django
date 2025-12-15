from django.urls import path
from .views import booking_view, booking_success_view

urlpatterns = [
    path("", booking_view, name="booking"),
    path("success/", booking_success_view, name="success"),
]
