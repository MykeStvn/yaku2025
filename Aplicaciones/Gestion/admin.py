from django.contrib import admin

from Aplicaciones.Gestion.models import Asistencia, Comunicado, Consumo, Detalle, Evento, Excedente, HistorialPropietario, Impuesto, Lectura, Medidor, Perfil, Recaudacion, Ruta, Socio, Tarifa, TipoEvento, Usuario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Socio)
admin.site.register(Tarifa)
admin.site.register(Excedente)
admin.site.register(Recaudacion)
admin.site.register(Asistencia)
admin.site.register(Comunicado)
admin.site.register(Consumo)
admin.site.register(Detalle)
admin.site.register(Evento)
admin.site.register(HistorialPropietario)
admin.site.register(Impuesto)
admin.site.register(Lectura)
admin.site.register(Medidor)
admin.site.register(Ruta)
admin.site.register(TipoEvento)








