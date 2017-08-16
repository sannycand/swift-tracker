from django.conf.urls import url

from .views import UserAPI

urlpatterns = [
    url(r'^signup/$', UserAPI.as_view({'post': 'signup'}), name="signup"),
    url(r'^login/$', UserAPI.as_view({'post': 'login'}), name="login"),
    url(r'^logout/$', UserAPI.as_view({'get': 'logout'}), name="logout"),
]