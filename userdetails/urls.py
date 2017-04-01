from django.conf.urls import url
from . import views

app_name = 'userdetails'

urlpatterns = [
    # /
    url(r'^$', views.UserFormView.as_view(), name='login'),
    url(r'^$', views.logout, name='logout'),
]
