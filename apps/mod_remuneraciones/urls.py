from django.urls import path
from . import views

urlpatterns = [
    path('remuneraciones/', views.index, name="index_remuneraciones"),
    path('remuneraciones/mutuales/', views.BoxList.as_view(), name='box_list'),
    path('remuneraciones/mutuales/view/<int:pk>', views.BoxView.as_view(), name='box_view'),
    path('remuneraciones/mutuales/new', views.BoxCreate.as_view(), name='box_new'),
    path('remuneraciones/mutuales/view/<int:pk>', views.BoxView.as_view(), name='box_view'),
    path('remuneraciones/mutuales/edit/<int:pk>', views.BoxUpdate.as_view(), name='box_edit'),
    path('remuneraciones/mutuales/delete/<int:pk>', views.BoxDelete.as_view(), name='box_delete'),
]
