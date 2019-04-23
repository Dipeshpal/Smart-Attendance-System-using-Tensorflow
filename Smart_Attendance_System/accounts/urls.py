from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    url(r'^profile/$', views.profile_view, name="profile"),
    url(r'^edit_profile/$', views.profile_edit, name="edit_profile"),
    url(r'^change_password/$', views.change_password, name="change_password"),
    url(r'apply/$', views.apply, name="apply"),
]
