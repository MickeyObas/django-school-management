from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .admin import custom_admin_site

urlpatterns = [
    path("admin/", custom_admin_site.urls),
    path("", include("pages.urls")),
    path("api/", include("api.urls")),
    path("accounts/", include("accounts.urls")),
    path("documents/", include("documents.urls")),
    path("department/", include("department.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
