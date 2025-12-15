from django.shortcuts import render, redirect
from .forms import BookingForm


# Create your views here.
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            print("Form errors:", form.errors)
        # no else here so form with errors remains available
    else:
        form = BookingForm()
    return render(request, "booking.html", {"form": form})


def booking_success_view(request):
    return render(request, "booking/success.html")

def index_view(request):
    form = BookingForm()
    return render(request, "index.html", {"form": form})
