from django.contrib.auth import get_user_model
from rest_framework import serializers

from app.book_clubs.models import BookClub

class BookClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class BookClubSerializer(serializers.ModelSerializer):
    owner = BookClubMemberSerializer(read_only=True)
    members = BookClubMemberSerializer(many=True, read_only=True)
    class Meta:
        model = BookClub
        fields = ('name', 'description', 'status', 'owner', 'members')


class CreateBookClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookClub
        fields = ('name', 'description')