from django.conf.urls import url
from django.views.generic import DetailView

from . import views
from .models import Photo

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^single/(?P<pk>\d+)/$',
        DetailView.as_view(model=Photo, template_name='photo/detail.html'),
        name='post_detail'),

]
