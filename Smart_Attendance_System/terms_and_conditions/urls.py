from django.conf.urls import url

from . import views

app_name = 'terms_and_conditions'

urlpatterns = [
    url(r'^$', views.terms_and_conditions, name="terms_and_conditions"),
]

