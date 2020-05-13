import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Product


def index(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'products/index.html', context)

def post1(request):
    if request.method == "GET":
        return render(request, 'products/post1.html', locals())
    if request.method == "POST":
        product = Product.objects.create(price=request.POST['price'],
                                        amount=request.POST['amount'])
        return HttpResponseRedirect(reverse_lazy('products:index'))
