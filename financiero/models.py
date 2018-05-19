from django.db import models

class Tecnica(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
class Sexo(models.Model):
    descripcion=models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion
class Grado(models.Model):
    descripcion=models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion
class Enfermedad(models.Model):
     descripcion=models.CharField(max_length=255)
     def __str__(self):
        return self.descripcion

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    tecnica = models.ForeignKey(Tecnica, on_delete = models.CASCADE)
    fecha_nacimiento = models.DateTimeField()
    sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete = models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, on_delete = models.CASCADE)
    eps = models.CharField(max_length=255)
    alergico = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nombre_madre = models.CharField(max_length=255)
    identificacion_madre = models.CharField(max_length=255)
    telefono_madre = models.CharField(max_length=255)
    nombre_padre = models.CharField(max_length=255)
    identificacion_padre = models.CharField(max_length=255)
    telefono_padre = models.CharField(max_length=255)
    nombre_emergencia = models.CharField(max_length=255)
    telefono_emergencia = models.CharField(max_length=255)
    nombre_retira_nino = models.CharField(max_length=255)
    telefono_retira_nino = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    tecnica = models.ForeignKey(Tecnica, on_delete = models.CASCADE)
    correo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class EstadoInstrumento(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion

class EstadoPago(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion

class EstadoAsistencia(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion

class Inventario(models.Model):
    instrumento = models.CharField(max_length=255)
    tecnica =   models.ForeignKey(Tecnica, on_delete = models.CASCADE)
    estado = models.ForeignKey(EstadoInstrumento, on_delete = models.CASCADE)
    observaciones = models.CharField(max_length=500)
    def __str__(self):
        return self.instrumento

class conceptoPago(models.Model):
    descripcion = models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion

class mes(models.Model):
    descripcion =  models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion

class PagoEstudiante(models.Model):
    concepto = models.ForeignKey(conceptoPago, on_delete = models.CASCADE)
    mes = models.ForeignKey(mes,on_delete = models.CASCADE)
    estado = models.ForeignKey(EstadoPago, on_delete = models.CASCADE)
    estudiante =  models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    cantidadPago = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True,blank=True,editable=False,null=True) 

    #def __str__(self):
    #    return self.estudiante
    


class PagoProfesor(models.Model):
    mes = models.CharField(max_length=255)
    estado = models.ForeignKey(EstadoPago, on_delete = models.CASCADE)
    profesor =  models.ForeignKey(Profesor, on_delete = models.CASCADE)
    cantidadPago = models.IntegerField()

class asistencia(models.Model):
    tecnica = models.ForeignKey(Tecnica, on_delete = models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
    estado =models.ForeignKey(EstadoAsistencia, on_delete = models.CASCADE)
    fecha = models.DateTimeField()