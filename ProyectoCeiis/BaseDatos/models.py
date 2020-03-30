from django.db import models

# Create your models here.

class Persona(models.Model):
     Id_Persona=models.CharField(max_length=200,primary_key=True)
     Nombres=models.CharField(max_length=200,null=False,blank=False)
     Apellido_Paterno=models.CharField(max_length=200,null=False,blank=False)
     Apellido_Materno=models.CharField(max_length=200,null=False,blank=False)
     Sexo=models.CharField(max_length=200,null=False,blank=False)

class Perfil(models.Model):
    Codigo_Perfil=models.AutoField(max_length=200,primary_key=True)
    Id_Persona=models.OneToOneField(Persona,max_length=200,on_delete=models.CASCADE)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Password=models.CharField(max_length=200,null=True,blank=True)
    Fecha_Creacion=models.DateField(auto_now_add=True)
    Fecha_Actualizacion=models.DateField(auto_now=True)

class Acceso(models.Model):
    Id_Acceso=models.AutoField(max_length=200,primary_key=True)
    Codigo_Perfil=models.OneToOneField(Perfil,on_delete=models.CASCADE)
    Nombre_Acceso=models.CharField(max_length=200,null=False,blank=False)

class Permiso(models.Model):
    Id_Permiso=models.AutoField(max_length=200,primary_key=True)
    Nombre_Permiso=models.CharField(max_length=200,blank=False,null=False)
    Descripcion=models.TextField(max_length=200,blank=True,null=True)

class Permisos_Acceso(models.Model):
    Id_Permiso_Acceso=models.AutoField(max_length=200,primary_key=True)
    Id_Acceso=models.ForeignKey(Acceso,on_delete=models.CASCADE)
    Id_Permiso=models.ForeignKey(Permiso,on_delete=models.CASCADE)

class Sesion(models.Model):
    Id_Sesion=models.AutoField(max_length=200,primary_key=True)
    Id_Perfil=models.ForeignKey(Perfil,on_delete=None)
    Fecha_Inicio=models.DateField()
    Hora_Inicio=models.DateTimeField()
    Fecha_Fin=models.DateField()
    Hora_Fin=models.DateTimeField()

class Estado_Sistema(models.Model):
    ID_Estado=models.AutoField(max_length=200,primary_key=True)
    Codigo_Perfil=models.ForeignKey(Perfil,on_delete=None)
    Id_Sesion=models.ForeignKey(Sesion,on_delete=None)
    Fecha_Cambio_Estado=models.DateField(auto_now=True)
    Hora_Cambio_Estado=models.DateTimeField(auto_now=True)
    Estado=models.CharField(max_length=200)

class Articulo(models.Model):
    Id_Articulo=models.AutoField(max_length=200,primary_key=True)
    Nombre_Articulo=models.CharField(max_length=200,null=False,blank=False)
    Tipo_Articulo=models.CharField(max_length=200,blank=False,null=False)

class Prestamo(models.Model):
    Id_Prestamo=models.AutoField(max_length=200,primary_key=True)
    Id_Persona=models.ForeignKey(Persona,on_delete=models.CASCADE)
    Id_Articulo=models.ForeignKey(Articulo,on_delete=models.CASCADE)
    Fecha_Prestamo=models.DateField(auto_now=True)
    Hora_Prestamo=models.DateTimeField(auto_now=True)
    Fecha_devoluvcion=models.DateField(auto_now_add=True)
    Hora_devolucion=models.DateTimeField(auto_now_add=True)
    Estado=models.CharField(max_length=200,blank=False,null=False)

class Multa(models.Model):
    Id_Multa=models.AutoField(max_length=200,primary_key=True)
    Id_Prestamo=models.ForeignKey(Prestamo,on_delete=models.CASCADE)
    Monto=models.FloatField(max_length=200,blank=False,null=True)
    Estado=models.CharField(max_length=200,blank=False,null=True)





