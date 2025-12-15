from django import forms
from .models import Booking
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "datetime", "people", "special_requests"]
        widgets = {
            "datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "special_requests": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_datetime(self):
        dt = self.cleaned_data["datetime"]
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt
