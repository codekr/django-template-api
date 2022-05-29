import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Django Admin typo configuration
admin.site.site_title = "Grocery Inc"
admin.site.site_header = "Grocery Administrator"
admin.site.index_title = "Welcome to Grocery Administrator"
admin.site.site_url = os.getenv('DJANGO_SITE_URL', 'http://localhost:8000/admin')

urlpatterns = [
                  # re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
                  # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  path('admin/', admin.site.urls),
                  path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
                  path("schema/", SpectacularAPIView.as_view(), name="schema"),
                  path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  re_path(r'^ht/', include('health_check.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)