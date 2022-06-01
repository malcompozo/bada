from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('account/', include('admin_user.api.urls')),
    path('swagger/', include('swagger.api.urls')),
    path('market/', include('bada_app.api.urls')),
    path('api/', include('default_event.api.urls')),
    path('api/', include('contact.api.urls')),
    path('api/', include('slider.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PERSONALIZAR ADMIN
admin.site.site_header = 'Bada Eventos'
admin.site.index_title = 'Panel de Administración'
admin.site.site_title = 'Bada Eventos'


