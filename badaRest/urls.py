from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bada_app.api.urls')),
    #path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PERSONALIZAR ADMIN
admin.site.site_header = 'Bada Eventos'
admin.site.index_title = 'Panel de Administración'
admin.site.site_title = 'Bada Eventos'


