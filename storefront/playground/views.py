from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import OrderItem
from store.models import Order
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    # keyword = value
    q = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('id')
    queryset = Product.objects.prefetch_related('promotions').order_by('title')
    return render(request, 'hello.html', {'name': 'exits', 'products': list(q)})
