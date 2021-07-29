from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Usuario,UbicacionMesa , Restaurante, Mesa, Reservacion,TiempoReserva
from .serializer import MesaSerializer,TiempoReservaSerializer,ReservacionSerializer,RestauranteSerializer,UbicacionMesaSerializer,UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UbicacionMesaViewSet(viewsets.ModelViewSet):
    queryset = UbicacionMesa.objects.all()
    serializer_class = UbicacionMesaSerializer

class RestauranteViewSet (viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

    @action(detail=True, methods=['get'])
    def Reservacion(self, request, pk=None):
        queryset = Reservacion.objects.filter(restaurante_id=pk)
        serializer = ReservacionSerializer(queryset, many=True)
        return Response(serializer.data) 

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

    @action(detail=True, methods=['get'])
    def Reservacion(self, request, pk=None):
        queryset = Reservacion.objects.filter(mesa_id=pk)
        serializer = MesaSerializer(queryset, many=True)
        return Response(serializer.data) 

class TiempoViewSet(viewsets.ModelViewSet):
    queryset = TiempoReserva.objects.all()
    serializer_class = TiempoReservaSerializer

    @action(detail=True, methods=['get'])
    def Reservacion(self, request, pk=None):
        queryset = Reservacion.objects.filter(hora_id=pk)
        serializer = TiempoReservaSerializer(queryset, many=True)
        return Response(serializer.data) 

class ReservacionViewSet(viewsets.ModelViewSet):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer