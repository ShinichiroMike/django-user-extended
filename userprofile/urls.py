from django.conf.urls import url
from .views import profile, user_edit

urlpatterns = [
	url(r'^profile/', profile, name='profile'),
    url(r'^edit/$', user_edit, name='user_edit')
]