from django.db import models
from users.models import User

class Doctor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    # telefono = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        
        db_table = "doctores"
        ordering = ["nombre"]
        

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nombre 
    
    class Meta:
        db_table = "especialidades"
        ordering = ["nombre"]


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nombre 
    
    class Meta:
        db_table = "tipos_documentos"
        ordering = ["nombre"]
        
        
class TipoSeguro(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nombre 
    
    class Meta:
        db_table = "tipos_seguros"
        ordering = ["nombre"]
        
class Paciente(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=8, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    tipo_seguro = models.ForeignKey(TipoSeguro, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        db_table = "pacientes"
        ordering = ["nombre"]

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    
    # def __str__(self):

    #     return self.fecha 
    
    class Meta:
        db_table = "citas"
