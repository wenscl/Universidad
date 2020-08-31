"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url

from app.views import index, update_data, imputacion, acumula, actividad, \
    login_user, logout_user, register_user, detail_patrimonio_neto, \
    detail_rentabilidad_actividad
from app.views_autocomplete import ImputacionImpuAcumulada, ImputacionImpuSimple, \
    ImputacionDescripcion, AcumulaImpuSimple, AcumulaImpuAcumulada, \
    ImputacionTipoMovim, ImputacionActividad, ImputacionTipoProveedor, \
    ImputacionProvincia

urlpatterns = [
    url(r'^acumula_impu_acumulada_autocomplete/$',
        AcumulaImpuAcumulada.as_view(),
        name='acumula_impu_acumulada_autocomplete'),
    url(r'^acumula_impu_simple_autocomplete/$', AcumulaImpuSimple.as_view(),
        name='acumula_impu_simple_autocomplete'),
    url(r'^imputacion_impu_simple_autocomplete/$',
        ImputacionImpuSimple.as_view(),
        name='imputacion_impu_simple_autocomplete'),
    url(r'^imputacion_impu_acumulada_autocomplete/$',
        ImputacionImpuAcumulada.as_view(),
        name='imputacion_impu_acumulada_autocomplete'),
    url(r'^imputacion_descripcion_autocomplete/$',
        ImputacionDescripcion.as_view(),
        name='imputacion_descripcion_autocomplete'),
    url(r'^imputacion_tipo_movim_autocomplete/$', ImputacionTipoMovim.as_view(),
        name='imputacion_tipo_movim_autocomplete'),
    url(r'^imputacion_actividad_autocomplete/$', ImputacionActividad.as_view(),
        name='imputacion_actividad_autocomplete'),
    url(r'^imputacion_tipo_proveedor_autocomplete/$',
        ImputacionTipoProveedor.as_view(),
        name='imputacion_tipo_proveedor_autocomplete'),
    url(r'^imputacion_provincia_autocomplete/$', ImputacionProvincia.as_view(),
        name='imputacion_provincia_autocomplete'),
    url(r'^register/$', register_user, name='register'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^$', index, name='index'),
    url(r'^update_db/$', update_data, name='update_db'),
    url(r'^imputacion/$', imputacion, name='imputacion'),
    url(r'^acumula/$', acumula, name='acumula'),
    url(r'^actividad/$', actividad, name='actividad'),
    url(r'^detalle_patrimonio_neto/$', detail_patrimonio_neto,
        name='detalle_patrimonio_neto'),
    url(r'^detalle_rentabilidad_actividad/$', detail_rentabilidad_actividad,
        name='detalle_rentabilidad_actividad'),
]
