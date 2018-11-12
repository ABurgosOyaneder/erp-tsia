"""erp_tsia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('', include('apps.mod_inventario.urls')),
    #path('', include('apps.mod_contabilidad.urls')),
    #path('', include('apps.mod_venta_cot.urls')),
    #path('', include('apps.mod_remuneraciones.urls')),
    #path('', include('apps.mod_facturacion.urls')),
    #path('', include('apps.mod_clientes.urls')),
    #path('', include('apps.mod_adquisiciones.urls')),
    path('admin/', admin.site.urls),
]
