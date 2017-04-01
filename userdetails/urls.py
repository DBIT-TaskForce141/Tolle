from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'userdetails'

urlpatterns = [
    # /
    url(r'^$', views.UserFormView.as_view(), name='login'),
    url(r'^$', views.logout, name='logout'),
    url(r'^journey/(?P<pk>\d+)/$', login_required(views.journey), name='journey'),
]
