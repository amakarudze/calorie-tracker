from django.shortcuts import redirect, render

from .models import Consume, Food
# Create your views here.


def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()

    foods = Food.objects.all()
    consumed_foods = Consume.objects.filter(user=request.user)
    return render(request, 'counter/index.html', {'foods': foods, 'consumed_foods': consumed_foods})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    else:
        return render(request, 'counter/delete.html')
