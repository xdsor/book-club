from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.users.serializers import UserPreviewSerializer


@api_view(['GET'], )
def self_user_info(request):
    if request.user.is_authenticated:
        user = UserPreviewSerializer(User.objects.get(pk=request.user.pk)).data
        return Response(user)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
