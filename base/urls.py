from django.contrib import admin
from django.urls import path
from base import views
urlpatterns = [
    path('', views.home, name='home'),
    path('Ourstory/',views.Our_story,name = 'about'),
    path('contact/',views.contact,name='contact'),
    path('ClassicsFlavours/',views.Classics_Flavours,name='Classics'),
    path('FruitnNuts/',views.Fruit_n_Nuts,name='FruitandNuts'),
    path('PremiumFlavours/',views.Premium_Flavours,name='Premium'),
    path('FancyFlavours/',views.Fancy_Flavours,name='Fancy'),
    path('Softy/',views.Sofy,name='Sofy'),
    path('Desserts/',views.Desserts,name='Desserts')

]