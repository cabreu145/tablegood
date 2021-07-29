from django.db import models
from core.utils import unique_folio_generator

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db.models.fields import SlugField
from django.db.models.signals import pre_save
import datetime as dt
# Create your models here.

class UsuarioManager(BaseUserManager):
    ''' Manager para Perfiles de Usuario '''

    def create_user(self, correo_electronico, usuario, nombre, apellido, fecha_nacimiento, telefono, rfc, password=None):
        """ Crear Nuevo perfil de Usuario """
        if not correo_electronico:
            raise ValueError('Usuario debe tener un correo')

        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, usuario=usuario, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, telefono=telefono, rfc=rfc)

        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self, correo_electronico, usuario, nombre, apellido, fecha_nacimiento, telefono, rfc, password):
        user = self.create_user(correo_electronico, usuario, nombre, apellido, fecha_nacimiento, telefono, rfc, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user

    


class Usuario(AbstractBaseUser, PermissionsMixin):
    """ Modelo Base de Datos para Usuarios en el Sistema"""
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefono = models.CharField( max_length=15)
    rfc = models.CharField(max_length=255, unique=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['usuario','nombre','apellido','fecha_nacimiento', 'telefono', 'rfc']

    def get_full_name(self):
        ''' Obtener Nombre Completo del Usuario'''
        return f'{self.nombre} {self.apellido} '

    ''' Obtener Nombre corto del Usuario'''
    def get_short_name(self):
        return self.nombre

    ''' Retornar Cadena Representando Nuestro Usuario'''
    def __str__(self):
        return self.correo_electronico

class Restaurante(models.Model):
    restaurante = models.TextField(max_length=7)

    def __str__(self):
        return self.restaurante

class UbicacionMesa(models.Model):
    ubicacion = models.TextField(max_length=7)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.ubicacion

class Mesa(models.Model):

    numero_mesa = models.IntegerField()
    
    ubicacion = models.ForeignKey(UbicacionMesa, on_delete=models.SET_NULL,null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL,null=True)
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.numero_mesa}'

class TiempoReserva(models.Model):
    hora = models.TimeField(default=dt.time(13, 00))


    def __str__(self):
        return f'Hora {self.hora}'

class Reservacion(models.Model):
    
    dia = models.DateField()
    hora = models.OneToOneField(TiempoReserva, on_delete=models.SET_NULL,null=True)
    folio = models.SlugField(max_length=200, null=True, blank=True)
    facturar = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL,null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL,null=True)
    ubicacion = models.ForeignKey(UbicacionMesa, on_delete=models.SET_NULL,null=True)

    class Meta:
        unique_together = [['dia','hora','mesa','usuario']]

    def __str__(self):
        return self.folio

def folio_generator(sender, instance, *args, **kwargs):
    if not instance.folio:
        instance.folio =  unique_folio_generator(instance)

pre_save.connect(folio_generator, sender = Reservacion)