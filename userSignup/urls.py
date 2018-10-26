from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from userSignup.signup import views as signup_views


urlpatterns = [
    url(r'^$', signup_views.home, name='home'),
    url(r'^login/$', auth_views.auth_login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', signup_views.signup, name='signup'),
]
