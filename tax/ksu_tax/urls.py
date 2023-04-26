from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:index>', views.result, name='result'),
    path('taxrate', views.taxrate, name= 'taxrate')

]