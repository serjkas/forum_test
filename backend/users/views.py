from django.db import connection
from rest_framework.response import Response
from machina.core.db.models import get_model
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from .serializers import ForumReadTrackSerializer, ForumSerializer, UserSerializer

ForumReadTrack = get_model('forum_tracking', 'ForumReadTrack')
Forum = get_model('forum', 'Forum')


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


@api_view(['GET'])
def get_users_forum(request):
    paginator = MyPagination()

    with connection.cursor() as cursor:
        query = """
        SELECT username, name FROM `test_db`.`forum_tracking_forumreadtrack` ft
        left join `test_db`.`auth_user` us on us.id = ft.user_id
        left join `test_db`.`forum_forum` fo on fo.id = ft.forum_id LIMIT 1000;
        """
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        resp = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    page = paginator.paginate_queryset(resp, request)
    return paginator.get_paginated_response(page)  


class ForumReadTrackModelViewSet(ModelViewSet):
    queryset = ForumReadTrack.objects.all()
    serializer_class = ForumReadTrackSerializer


class ForumModelViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer