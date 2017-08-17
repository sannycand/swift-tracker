from django.conf.urls import url

from .views import UserAPI, AuthUserAPI

urlpatterns = [
    url(r'^signup/$', UserAPI.as_view({'post': 'signup'}), name="signup"),
    url(r'^login/$', UserAPI.as_view({'post': 'login'}), name="login"),
    url(r'^logout/$', UserAPI.as_view({'get': 'logout'}), name="logout"),
    url(r'^auth/user/$', AuthUserAPI.as_view({'get': 'user'}), name="current-user"),
]