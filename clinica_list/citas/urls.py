from django.urls import path, include
from .views import home, CitasUpdate, CitasDelete, PacienteCreate, CitasCreate, CitasList, PacienteUpdate, PacienteList, TipoSeguroUpdate, TipoSeguroCreate, TipoSeguroDelete, TipoSeguroList , TipoDocumentoUpdate , TipoDocumentoCreate, TipoDocumentoDelete, TipoDocumentoList, DoctorList, DoctorCreate, DoctorDelete, DoctorUpdate, EspecialidadList, EspecialidadDelete, EspecialidadUpdate , EspecialidadCreate

urlpatterns = [
    path("", home, name="home"),
    # DOCTORES
    path("doctor/", DoctorList.as_view(), name="doctor"),
    path("doctor/create/", DoctorCreate.as_view(), name="doctor-create"),
    path("DoctorUpdate/<int:pk>/", DoctorUpdate.as_view(), name="doctor-update"),
    path("DoctorDelete/<int:pk>/", DoctorDelete.as_view(), name="doctor-delete"),
    # ESPECIALIDADES
    path("especialidad/", EspecialidadList.as_view(), name="especialidad"),
    path("EspecialidadDelete/<int:pk>/", EspecialidadDelete.as_view(), name="especialidad-delete"),
    path("especialidad/create/", EspecialidadCreate.as_view(), name="especialidad-create"),
    path("EspecialidadUpdate/<int:pk>/", EspecialidadUpdate.as_view(), name="especialidad-update"),
    # TIPOS DOCUMENTO
    path("tipo_documento/", TipoDocumentoList.as_view(), name="tipo_documento"),
    path("TipoDocDelete/<int:pk>/", TipoDocumentoDelete.as_view(), name="documento-delete"),
    path("TipoDoc/create/", TipoDocumentoCreate.as_view(), name="documento-create"),
    path("TipoDocUpdate/<int:pk>/", TipoDocumentoUpdate.as_view(), name="documento-update"),
    # TIPOS SEGURO
    path("tipo_seguro/", TipoSeguroList.as_view(), name="tipo_seguro"),
    path("TipoSegDelete/<int:pk>/", TipoSeguroDelete.as_view(), name="seguros-delete"),
    path("TipoSeguro/create/", TipoSeguroCreate.as_view(), name="seguros-create"),
    path("TipoSegUpdate/<int:pk>/", TipoSeguroUpdate.as_view(), name="seguros-update"),
    # PACIENTES
    path("paciente/", PacienteList.as_view(), name="paciente"),
    path("PacienteUpdate/<int:pk>/", PacienteUpdate.as_view(), name="paciente-update"),
    path("Paciente/create/", PacienteCreate.as_view(), name="paciente-create"),
    # CITAS
    path("citas/", CitasList.as_view(), name="citas"),
    path("Cita/create/", CitasCreate.as_view(), name="cita-create"),
    path("CitasDelete/<int:pk>/", CitasDelete.as_view(), name="cita-delete"),
    path("CitasUpdate/<int:pk>/", CitasUpdate.as_view(), name="cita-update"),
]
