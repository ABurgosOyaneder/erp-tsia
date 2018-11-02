from django.urls import path
from . import views

urlpatterns = [
    path('remuneraciones/', views.index, name="index_remuneraciones")
]