from django.contrib import admin
from .models import Doctor, Especialidad, TipoDocumento, TipoSeguro, Paciente, Cita

admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(TipoDocumento)
admin.site.register(TipoSeguro)
admin.site.register(Paciente)
admin.site.register(Cita)


