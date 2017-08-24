from django.conf.urls import url

from .views import ProjectMemberAPI, LogAPI, ProjectAPI

urlpatterns = [
    url(r'^$', ProjectAPI.as_view({'get': 'projects'}), name="projects"),
    url(r'^add/$', ProjectAPI.as_view({'post': 'add_project'}), name="add-project"),
    url(r'^(?P<project_id>\d+)/users/$', ProjectAPI.as_view({'get': 'users'}), name="users"),
    url(r'^add/member/$', ProjectAPI.as_view({'post': 'add_member'}), name="add-member"),
    url(r'^member/$', ProjectMemberAPI.as_view({'get': 'user_projects'}), name="user-projects"),
    url(r'^(?P<project_id>\d+)/log/$', LogAPI.as_view({'post': 'start_log'}), name="start-log"),
    url(r'^stop/log/$', LogAPI.as_view({'put': 'stop_log'}), name="stop-log"),
    url(r'^current/log/$', LogAPI.as_view({'get': 'current_log'}), name="current-log"),
]



