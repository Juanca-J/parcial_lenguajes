from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Doctor, Especialidad, TipoDocumento, TipoSeguro, Paciente, Cita
from django.urls import reverse_lazy

def home(request):
    return render(request, "home.html")

class CitasList(ListView):
    model = Cita
    context_object_name = "citas"

class CitasCreate(CreateView):
    model = Cita
    fields = ["fecha", "hora", "doctor", "paciente", "especialidad"]
    success_url = reverse_lazy("citas") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CitasCreate, self).form_valid(form)

class CitasDelete(DeleteView):
    model = Cita
    success_url = reverse_lazy("citas")
    
    def form_valid(self, form):
        return super(CitasDelete, self).form_valid(form)

class CitasUpdate(UpdateView):
    model = Cita
    fields = ["fecha", "hora", "doctor", "paciente", "especialidad"]
    success_url = reverse_lazy("citas") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CitasUpdate, self).form_valid(form)

class PacienteList(ListView):
    model = Paciente
    context_object_name = "paciente"

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ["nombre", "apellido", "fecha_nacimiento", "direccion", "tipo_documento", "numero_documento", "tipo_seguro", "tipo_seguro"]
    success_url = reverse_lazy("paciente") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PacienteUpdate, self).form_valid(form)

class PacienteCreate(CreateView):
    model = Paciente
    fields = ["nombre", "apellido", "fecha_nacimiento", "direccion", "tipo_documento", "numero_documento", "tipo_seguro", "tipo_seguro"]
    success_url = reverse_lazy("paciente") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PacienteCreate, self).form_valid(form)

class TipoSeguroList(ListView):
    model = TipoSeguro
    context_object_name = "tipo_seguro"

class TipoSeguroCreate(CreateView):
    model = TipoSeguro
    fields = ["nombre"]
    success_url = reverse_lazy("tipo_seguro") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TipoSeguroCreate, self).form_valid(form)
    
class TipoSeguroUpdate(UpdateView):
    model = TipoSeguro
    fields = ["nombre"]
    success_url = reverse_lazy("tipo_seguro") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TipoSeguroUpdate, self).form_valid(form)

class TipoSeguroDelete(DeleteView):
    model = TipoSeguro
    success_url = reverse_lazy("tipo_seguro")
    
    def form_valid(self, form):
        return super(TipoSeguroDelete, self).form_valid(form)


class TipoDocumentoList(ListView):
    model = TipoDocumento
    context_object_name = "tipo_documento"

class TipoDocumentoCreate(CreateView):
    model = TipoDocumento
    fields = ["nombre"]
    success_url = reverse_lazy("tipo_documento") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TipoDocumentoCreate, self).form_valid(form)

class TipoDocumentoUpdate(UpdateView):
    model = TipoDocumento
    fields = ["nombre"]
    success_url = reverse_lazy("tipo_documento") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TipoDocumentoUpdate, self).form_valid(form)

class TipoDocumentoDelete(DeleteView):
    model = TipoDocumento
    success_url = reverse_lazy("tipo_documento")
    
    def form_valid(self, form):
        return super(TipoDocumentoDelete, self).form_valid(form)




class DoctorList(ListView):
    model = Doctor
    context_object_name = "doctor"

# class DoctorDetail(ListView):
#     model = Doctor
#     context_object_name = "doctor"
#     template_name = "doc"
    
class DoctorCreate(CreateView):
    model = Doctor
    fields = ["nombre", "telefono", "direccion"]
    success_url = reverse_lazy("doctor") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DoctorCreate, self).form_valid(form)

class DoctorUpdate(UpdateView):
    model = Doctor
    fields = ["nombre", "telefono", "direccion"]
    success_url = reverse_lazy("doctor") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DoctorUpdate, self).form_valid(form)

class DoctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctor")
    
    def form_valid(self, form):
        return super(DoctorDelete, self).form_valid(form)


class EspecialidadList(ListView):
    model = Especialidad
    context_object_name = "especialidad"

class EspecialidadCreate(CreateView):
    model = Especialidad
    fields = ["nombre"]
    success_url = reverse_lazy("especialidad") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EspecialidadCreate, self).form_valid(form)

class EspecialidadUpdate(UpdateView):
    model = Especialidad
    fields = ["nombre"]
    success_url = reverse_lazy("especialidad") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EspecialidadUpdate, self).form_valid(form)

class EspecialidadDelete(DeleteView):
    model = Especialidad
    success_url = reverse_lazy("especialidad")
    
    def form_valid(self, form):
        return super(EspecialidadDelete, self).form_valid(form)