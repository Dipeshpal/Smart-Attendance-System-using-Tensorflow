from django.conf.urls import url

from . import views

app_name = 'contact_us'

urlpatterns = [
    url(r'^', views.contact_us, name="contact_us"),
]

