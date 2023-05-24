from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path('quarted_data',views.annual_data,name='quarted_data')
]