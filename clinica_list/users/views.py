from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.views.generic import ListView, UpdateView
from users.models import User
from django.urls import reverse_lazy

# Create your views here.

class UserList(ListView):
    model = User
    context_object_name = "users"

class UserUpdate(UpdateView):
    model = User
    fields = [ "full_name", "email"]
    success_url = reverse_lazy("user") 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserUpdate, self).form_valid(form)
    
# class CitasUpdate(UpdateView):
#     model = Cita
#     fields = ["fecha", "hora", "doctor", "paciente", "especialidad"]
#     success_url = reverse_lazy("citas") 
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(CitasUpdate, self).form_valid(form)

    

def login_user(request):
    form = LoginForm()
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Metodo:", request.method)
            cd = form.cleaned_data  # recupera la data limpia
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = f"Hola { user.username}!! Te has logueado"
                    return render(request, "home.html", {"user:": user})
                else:
                    message = "El usuario ingresado no se encuentra activo"
            else:
                message = "Cuenta inválida"

    return render(
        request, "users/login.html", context={"form": form, "messages": message}
    )
  
def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/registro.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f"Tu cuenta ha sido creada")
            login(request, user)

            return redirect("home")
        else:
            messages.error(request, f"Error al crear tu cuenta")
            return render(request, "users/registro.html", {"form": form})
    

def sign_out(request):
    logout(request)
    messages.success(request, f"Tu sesión ha sido cerrada")
    return redirect("home")
