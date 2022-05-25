from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Bada API",
        default_version='v1',
        description="Welcome to Bada Rest API",
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('bada_app.api.urls')),
    path('api/', include('default_event.api.urls')),
    path('api/', include('contact.api.urls')),
    path('api/', include('slider.api.urls')),
    #path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PERSONALIZAR ADMIN
admin.site.site_header = 'Bada Eventos'
admin.site.index_title = 'Panel de Administración'
admin.site.site_title = 'Bada Eventos'


