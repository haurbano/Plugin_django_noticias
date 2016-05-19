from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin

from .models import DestinosPluginModel
#from destinos_plugin.models import DestinosPluginModel

class DestinosPluginPublisher(CMSPluginBase):
    model = DestinosPluginModel
    name = "Destinos de viaje"
    render_template = "djangocms_destinos/destinos_plugin.html"
    cache = False

    def render(self,context,instance,placeholder):
        context = super(DestinosPluginPublisher, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(DestinosPluginPublisher)
