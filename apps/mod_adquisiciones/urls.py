from django.urls import path
from . import views


#Aqui van la urls de su modulo
urlpatterns = [
    path('adquisiciones/', views.index, name="index_adquisiciones")
]
