from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView, PostListView, PostRetrieveView

routers = routers.DefaultRouter()
routers.register('tasks', TaskViewSet , basename='tasks')

urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(routers.urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)