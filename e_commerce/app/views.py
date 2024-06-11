from django.shortcuts import render
from app.models import Product,Image

# Create your views here.


def index(request):
    products = Product.objects.all()
    images = Image.objects.all()
    context = {'products': products, 'images': images}
    return render(request, 'app/product-list.html', context)


def product_detail(request):
    return render(request, 'app/product-details.html')
