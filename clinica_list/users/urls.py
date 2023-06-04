from django.urls import path, include
from .import views  
from .views import UserList, UserUpdate

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("registro/", views.register_user, name="registro"),
    path("logout/", views.sign_out, name="logout"),
    
    path("user/", UserList.as_view(), name="user"),
    path("UserUpdate/<str:pk>/", UserUpdate.as_view(), name="user-update"),
    
    #     path("EspecialidadUpdate/<int:pk>/", EspecialidadUpdate.as_view(), name="especialidad-update"),


]


