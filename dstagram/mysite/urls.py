from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from photo.views import post_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='home'),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
