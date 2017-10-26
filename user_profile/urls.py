from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

# logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userprofile.urls', namespace='user')),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^login/', login, {'template_name':'index.html'}, name='login'),
]
