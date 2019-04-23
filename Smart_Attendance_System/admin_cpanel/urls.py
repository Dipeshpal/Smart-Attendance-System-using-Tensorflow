from django.conf.urls import url

from . import views


app_name = 'admin_cpanel'

urlpatterns = [
    url(r'^', views.admin_cpanel, name="admin_cpanel"),
]

