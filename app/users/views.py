from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.users.serializers import UserSelfInfoSerializer


@api_view(['GET'], )
def self_user_info(request):
    if request.user.is_authenticated:
        user = request.user
        clubs = request.user.member_clubs.all()
        serializer = UserSelfInfoSerializer({
            'id': user.id,
            'username': user.username,
            'book_clubs': clubs,
        })
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)