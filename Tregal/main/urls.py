from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_info_view, name='contact'),
    path('services/', services, name='services'),
    path('tour/', tour_packages, name='tour_packages'),
    path('scholarships/', scholarships, name='scholarships'),
    path('mission/', mission, name='mission'),
    path('special-offers/', special_offers, name='special_offers'),
]
