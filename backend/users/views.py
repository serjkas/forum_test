
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from django.db import connection


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

    
