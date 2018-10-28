from django.urls import path
from . import views

urlpatterns = [
    path('contabilidad/', views.index, name="index_contabilidad")
]