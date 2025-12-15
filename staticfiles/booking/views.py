from django.shortcuts import render


# Create your views here.
def booking_view(request):
    return render(request, "booking.html")
