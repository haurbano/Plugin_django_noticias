from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField

class Destino(models.Model):
    nombre = models.TextField(default="Destino")
    descripcion = models.TextField(default="descripcion")
    valor = models.TextField(default="0000")
    itinerario = models.TextField(default="itinerario")
    numero_contacto = models.TextField(default="3105555")
    placeholderimgs = PlaceholderField('Imagenes', related_name='images_placeholder')
    placeholdercontact = PlaceholderField('Contacto',related_name='contact_placeholder')
    photo_inicial = FilerImageField(blank=True, null=True, help_text='Optional. Image for news article.', on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.nombre



# Create your models here.
class DestinosPluginModel(CMSPlugin):
    user_name = models.CharField(max_length=200, default='Hamilton')
    list_destinos = Destino.objects.all()
