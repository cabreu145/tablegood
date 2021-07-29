from rest_framework import serializers

from .models import Usuario,UbicacionMesa , Restaurante, Mesa, Reservacion,TiempoReserva

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        

class UbicacionMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionMesa
        fields = '__all__'


class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = 'restaurante'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = 'ubicacionS'

class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = 'dia','hora' ,'folio','facturar','usuario','restaurante','mesa','ubicacion'
    

class TiempoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiempoReserva
        fields = '__all__'
