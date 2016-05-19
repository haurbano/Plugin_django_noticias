from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<destino_id>[0-9]+)/$', views.detalleDestino, name='detalle'),
]
