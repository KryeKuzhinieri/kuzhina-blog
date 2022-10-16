from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Markdown editor
    path("", include('blog.urls'))
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
