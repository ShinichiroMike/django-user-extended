from django.conf.urls import url
from .views import profile, signup, user_edit

urlpatterns = [
	url(r'^profile/', profile, name='profile'),
    url(r'^signup/', signup, name='signup'),
    url(r'^edit/(?P<user_id>\d+)/$', user_edit, name='user_edit')
]