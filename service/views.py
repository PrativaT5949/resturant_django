from django.shortcuts import render
from .models import Service


# Create your views here.
def service_view(request):
    service = Service.objects.all()
    return render(request, "service.html")
