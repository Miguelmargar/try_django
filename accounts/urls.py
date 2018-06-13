#accounts urls.py
#this file is linked to the urls.py file in try_django which is the main urls.py file

from django.conf.urls import url
from accounts.views import login, register, logout, profile
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^login', login, name="login"),#no $ for the password reset redirect function to work properly
    url(r'^register$', register, name="register"),
    url(r'^logout$', logout, name="logout"),
    url(r'^profile$', profile, name="profile"),
    #all the below urls are for password reset functionality
    url(r'^password-reset/$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
]