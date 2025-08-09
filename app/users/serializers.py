from django.contrib.auth import get_user_model
from rest_framework import serializers

from app.book_clubs.models import BookClub

class UserSelfInfoBookClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']

class UserSelfInfoBookClubsSerializer(serializers.ModelSerializer):
    owner = UserSelfInfoBookClubMemberSerializer(read_only=True)
    members = UserSelfInfoBookClubMemberSerializer(many=True, read_only=True)
    class Meta:
        model = BookClub
        fields = ('id' ,'name', 'description', 'status', 'owner', 'members')


class UserSelfInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    book_clubs = UserSelfInfoBookClubsSerializer(many=True, read_only=True)