from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
