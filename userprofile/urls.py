from django.conf.urls import url
from .views import profile, user_edit

# restringir signup cuando estas logeado
urlpatterns = [
	url(r'^profile/', profile, name='profile'),
    url(r'^edit/$', user_edit, name='user_edit')
]