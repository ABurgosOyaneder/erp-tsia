from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="index_adquisiciones"),
    path('adquisiciones/', views.adquisiciones, name="adquisiciones_adquisiciones"),
    path('compras/', views.compras, name="compras_adquisiciones"),
]

