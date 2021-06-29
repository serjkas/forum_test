from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import get_users_forum, ForumReadTrackModelViewSet, ForumModelViewSet, UserModelViewSet

router = SimpleRouter()

router.register(r'forum_read_track', ForumReadTrackModelViewSet, basename='ForumReadTrackModelViewSet')
router.register(r'forum_name', ForumModelViewSet, basename='ForumModelViewSet')
router.register(r'user_name', UserModelViewSet, basename='UserModelViewSet')

urlpatterns = [
    path('get_users_forum', get_users_forum),
]

urlpatterns += router.urls