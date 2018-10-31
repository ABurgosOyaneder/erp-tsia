from django.urls import path
from . import views

urlpatterns = [
    path('adquisiciones/',views.index, name="index_adquisiciones")
]