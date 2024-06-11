from django.urls import path
from app.views import index, product_detail


urlpatterns = [
    path('', index, name='index'),
    path('p/', product_detail, name='product_detail')
]
