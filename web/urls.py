from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'profile/(?P<usrname>[A-z -]+)$', views.profile, name="profile"),
    url(r'^logout', views.user_logout, name="logout"),
]
