from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact_view, name='contact'),
    path('diamond/', views.diamond, name='diamond'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('gold/', views.gold, name='gold'),
    path('premium/', views.premium, name='premium'),
    path('services/', views.services, name='services'),
    path('thankyou/', views.thankyou, name='thankyou'),  # URL name matches redirect
    path('contacts-map/', views.contacts_map, name='contacts_map'),
]
