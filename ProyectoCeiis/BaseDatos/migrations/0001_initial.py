# Generated by Django 2.1.12 on 2020-03-29 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('Id_Acceso', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Nombre_Acceso', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('Id_Articulo', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Nombre_Articulo', models.CharField(max_length=200)),
                ('Tipo_Articulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Sistema',
            fields=[
                ('ID_Estado', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Fecha_Cambio_Estado', models.DateField(auto_now=True)),
                ('Hora_Cambio_Estado', models.DateTimeField(auto_now=True)),
                ('Estado', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('Id_Multa', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Monto', models.FloatField(max_length=200, null=True)),
                ('Estado', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('Codigo_Perfil', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Password', models.CharField(blank=True, max_length=200, null=True)),
                ('Fecha_Creacion', models.DateField(auto_now_add=True)),
                ('Fecha_Actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('Id_Permiso', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Nombre_Permiso', models.CharField(max_length=200)),
                ('Descripcion', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permisos_Acceso',
            fields=[
                ('Id_Permiso_Acceso', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Id_Acceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Acceso')),
                ('Id_Permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('Id_Persona', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=200)),
                ('Apellido_Paterno', models.CharField(max_length=200)),
                ('Sexo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('Id_Prestamo', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Fecha_Prestamo', models.DateField(auto_now=True)),
                ('Hora_Prestamo', models.DateTimeField(auto_now=True)),
                ('Fecha_devoluvcion', models.DateField(auto_now_add=True)),
                ('Hora_devolucion', models.DateTimeField(auto_now_add=True)),
                ('Estado', models.CharField(max_length=200)),
                ('Id_Articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Articulo')),
                ('Id_Persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('Id_Sesion', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('Fecha_Inicio', models.DateField()),
                ('Hora_Inicio', models.DateTimeField()),
                ('Fecha_Fin', models.DateField()),
                ('Hora_Fin', models.DateTimeField()),
                ('Id_Perfil', models.ForeignKey(on_delete=None, to='BaseDatos.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='Id_Persona',
            field=models.OneToOneField(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Persona'),
        ),
        migrations.AddField(
            model_name='multa',
            name='Id_Prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Prestamo'),
        ),
        migrations.AddField(
            model_name='estado_sistema',
            name='Codigo_Perfil',
            field=models.ForeignKey(on_delete=None, to='BaseDatos.Perfil'),
        ),
        migrations.AddField(
            model_name='estado_sistema',
            name='Id_Sesion',
            field=models.ForeignKey(on_delete=None, to='BaseDatos.Sesion'),
        ),
        migrations.AddField(
            model_name='acceso',
            name='Codigo_Perfil',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BaseDatos.Perfil'),
        ),
    ]