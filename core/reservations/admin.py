from django.contrib import admin

from .models import  Usuario,UbicacionMesa , Restaurante, Mesa, Reservacion,TiempoReserva
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class UbicacionesAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('id','restaurante')

class UbicacionMesaAdmin(admin.ModelAdmin):
    list_display = ('id','ubicacion')

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('id','folio')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Mesa)
admin.site.register(TiempoReserva)
admin.site.register(UbicacionMesa, UbicacionMesaAdmin)
admin.site.register(Restaurante,RestauranteAdmin)
admin.site.register(Reservacion, ReservacionAdmin)