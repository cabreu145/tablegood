# Generated by Django 3.2.5 on 2021-07-28 22:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuario', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('telefono', models.CharField(max_length=15)),
                ('rfc', models.CharField(max_length=255, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurante', models.TextField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='TiempoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(default=datetime.time(13, 0))),
            ],
        ),
        migrations.CreateModel(
            name='UbicacionMesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.TextField(max_length=7)),
                ('restaurante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mesa', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
                ('restaurante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.restaurante')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.ubicacionmesa')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('folio', models.SlugField(blank=True, max_length=200, null=True)),
                ('facturar', models.BooleanField(default=False)),
                ('hora', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.tiemporeserva')),
                ('mesa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.mesa')),
                ('restaurante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.restaurante')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.ubicacionmesa')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('dia', 'hora', 'mesa', 'usuario')},
            },
        ),
    ]
