from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getproducts/', views.getproducts, name='products'),
    path('productdetails/<int:id>', views.productdetails, name='productdetails'),
    path('newProduct/', views.newProduct, name='newproduct'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]