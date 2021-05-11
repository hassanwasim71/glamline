from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index,name='index'),
    path('prodpage/', views.productpage,name='productpage'),
    path("proddet/<int:myid>", views.proddet,name="productdetails"),
    path('contact/', views.contact,name='Contactus'),
    path('about/', views.about,name='about'),
    path('search/', views.search,name='search'),

    path('tracker/', views.track,name='tracker'),
    path('checkout/', views.checkout,name='checkout'),
    path('blog/', views.blog,name='blog'),
    path('blogdet/<int:myid>', views.blogdet,name='blogdet'),
]
