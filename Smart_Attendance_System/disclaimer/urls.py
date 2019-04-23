from django.conf.urls import url

from . import views

app_name = 'disclaimer'

urlpatterns = [
    url(r'^', views.disclaimer, name="disclaimer"),
]

