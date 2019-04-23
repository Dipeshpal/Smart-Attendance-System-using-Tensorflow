from django.conf.urls import url

from . import views


app_name = 'videos'

urlpatterns = [
    url(r'^', views.videos_page, name="videos_page"),
]

