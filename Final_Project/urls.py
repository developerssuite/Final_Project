from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from products import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.home),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r"^search/", include("watson.urls", namespace="watson")),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
