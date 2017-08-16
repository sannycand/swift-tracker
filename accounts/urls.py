from django.conf.urls import url

from .views import UserAPI

urlpatterns = [
    url(r'^signup/$', UserAPI.as_view({'post': 'signup'}), name="signup"),
]