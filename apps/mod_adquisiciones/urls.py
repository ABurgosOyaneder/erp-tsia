from django.urls import path
from . import views

from apps.mod_adquisiciones.views import AdquisicionesList

urlpatterns = [
    path('index/', views.index, name="index_adquisiciones"),
    path('adquisiciones/', AdquisicionesList.as_view(), name="adquisiciones_adquisiciones"),
    path('compras/', views.compras, name="compras_adquisiciones"),
]

