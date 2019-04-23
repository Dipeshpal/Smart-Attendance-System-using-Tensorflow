from django.conf.urls import url

from . import views

app_name = 'face_recognition'

urlpatterns = [
    url(r'^$', views.face_recognition, name="face_recognition"),
    url(r'^training/$', views.training, name="training"),
]
