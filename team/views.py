from django.shortcuts import render
from .models import TeamMember


# Create your views here.
def team_view(request):
    members = TeamMember.objects.all()
    return render(request, "team.html", {"members": members})
