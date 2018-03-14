from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profiles/(?P<usrname>[A-z-]{1,32})$',
        views.get_delete_update_profile,
        name='get_delete_update_profile'),
    url(r'^profiles/$',
        views.get_post_profiles,
        name='get_post_profiles')
]
