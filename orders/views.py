from django.shortcuts import render
from .models import Order

# Create your views here.

# return http response
def new(request):
    orders = Order.objects.filter(status='new')
    return render(request, 'orders/new.html', {'orders': orders})

def preparing(request):
    orders = Order.objects.filter(status='preparing')
    return render(request, 'orders/preparing.html', {'orders': orders})

def completed(request):
    orders = Order.objects.filter(status='completed')
    return render(request, 'orders/completed.html', {'orders': orders})

# single view
def single(request, id):
    order = Order.objects.get(id=id)

    if request.method == "POST":
        post_id = request.POST.get('order-new')
        user_id = request.POST.get('order-preparing')

        if post_id:
            order.status = 'preparing'
            order.save()
        elif user_id:
            order.status = 'completed'
            order.save()
    

    return render(request, 'orders/single.html', {'order': order})
