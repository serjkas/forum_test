
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db import connection


@api_view(['GET'])
def get_users_forum(request):
    with connection.cursor() as cursor:
        query = """
        SELECT username, name FROM `test_db`.`forum_tracking_forumreadtrack` ft
        left join `test_db`.`auth_user` us on us.id = ft.user_id
        left join `test_db`.`forum_forum` fo on fo.id = ft.forum_id LIMIT 1000;
        """
        cursor.execute(query)
        row = cursor.fetchone()

        columns = [col[0] for col in cursor.description]
        resp = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    if resp:
        return Response(resp)
    else:
        return Response('Not found users')    

    
