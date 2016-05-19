from django.shortcuts import render
from .models import Destino
from filer.fields.image import FilerImageField

# Create your views here.
def detalleDestino(request, destino_id):
    destino = Destino.objects.get(pk=destino_id)
    context = {
        'destino':destino,
    }
    return render(request, 'djangocms_destinos/detalle_destino.html', context)
