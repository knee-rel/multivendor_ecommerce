# IMS/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import include, path

urlpatterns = [
    path("/", include("inventory.urls")),
    path("admin/", admin.site.urls),
    path(
        "", auth.LoginView.as_view(template_name="inventory/login.html"), name="login"
    ),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="inventory/logout.html"),
        name="logout",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
