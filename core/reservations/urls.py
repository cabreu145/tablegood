from django.conf.urls import url
from django.urls import path

from rest_framework import routers

from .viewsets import UsuarioViewSet, MesaViewSet, UbicacionMesaViewSet, RestauranteViewSet, TiempoViewSet,ReservacionViewSet

route = routers.SimpleRouter()
route.register('usuario',UsuarioViewSet)
route.register('mesa',MesaViewSet)
route.register('ubicacion',UbicacionMesaViewSet)
route.register('restaurante',RestauranteViewSet)
route.register('tiempo',TiempoViewSet)
route.register('reservacion',ReservacionViewSet)

urlpatterns = route.urls