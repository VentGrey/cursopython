from django.shortcuts import render
from .models import Homework, Image

def home(request):
    homeworks = Homework.objects.all()
    images = Image.objects.all()
    return render(request, 'core/home.html', {'homeworks': homeworks, 'images': images})
