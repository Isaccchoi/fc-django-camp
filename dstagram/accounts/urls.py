from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from accounts.views import register

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^register/$', register, name='register'),
]
