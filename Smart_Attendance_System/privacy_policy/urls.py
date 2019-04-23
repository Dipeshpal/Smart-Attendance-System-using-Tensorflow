from django.conf.urls import url

from . import views

app_name = 'privacy_policy'

urlpatterns = [
    url(r'^', views.privacy_policy, name="privacy_policy"),
]

