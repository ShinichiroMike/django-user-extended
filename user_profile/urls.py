from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from userprofile.views import signup
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userprofile.urls', namespace='user')),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^login/', user_passes_test(lambda u: u.is_anonymous, login_url='/user/profile')(login), {'template_name':'index.html'}, name='login'),
    url(r'^signup/', signup, name='signup'),
]
