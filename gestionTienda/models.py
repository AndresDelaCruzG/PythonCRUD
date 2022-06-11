from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    caducidad = models.DateField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)  # llave foranea

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    numero_orden = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()
    articulos_orden = models.ManyToManyField(Producto)  # muchos a muchos


class TipoEmpleado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    sueldo = models.FloatField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)  # llave foranea


class Sugerencia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)


class Directorio(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    referencia = models.CharField(max_length=100)