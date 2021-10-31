from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})
