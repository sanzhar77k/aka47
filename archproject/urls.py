from django.contrib import admin
from django.urls import path, include  # Import the include function


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change-language/', set_language, name='set_language'),
    path('', include('main.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)