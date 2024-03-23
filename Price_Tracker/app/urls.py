from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:pk>', views.pdelete, name="delete"),
    path('update/', views.update_price, name="update"),
    
]