from django.conf.urls import url

from .views import ProjectMemberAPI

urlpatterns = [
    url(r'^member/$', ProjectMemberAPI.as_view({'get': 'user_projects'}), name="user-projects"),
]