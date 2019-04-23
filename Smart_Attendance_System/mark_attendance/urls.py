from django.conf.urls import url

from . import views

app_name = 'mark_attendance'

urlpatterns = [
    url(r'^success/$', views.mark_attendance_success, name="success"),
    url(r'^$', views.mark_attendance, name="mark_attendance"),
    url(r'^camera_attendance', views.camera_attendance, name="camera_attendance"),
]
