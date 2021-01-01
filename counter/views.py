from django.shortcuts import render

from .models import Food
# Create your views here.


def index(request):
    foods = Food.objects.all()
    return render(request, 'counter/index.html', {'foods': foods})
