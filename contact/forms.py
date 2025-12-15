from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["fullname", "email_address", "subject", "message"]
        widgets = {
            "fullname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email_address": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Message",
                    "style": "height:150px",
                }
            ),
        }
