from django.conf.urls import url

from . import views

app_name = 'fetch_data'

urlpatterns = [
    url(r'^$', views.fetch_data, name="fetch_data"),
]
