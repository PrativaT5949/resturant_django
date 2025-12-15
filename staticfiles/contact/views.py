from django.shortcuts import render


# Create your views here.
def Contact_view(request):
    return render(request, "contact.html")
