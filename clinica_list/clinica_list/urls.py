
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path("", include("users.urls")),
    path("", include("citas.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
