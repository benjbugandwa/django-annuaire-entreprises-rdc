from django.urls import path
from .views import recherche, detail_entreprise
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("", recherche, name="recherche"),
    path("entreprise/<uuid:id>/", detail_entreprise, name="entreprise_detail"),
]

urlpatterns =+ staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )