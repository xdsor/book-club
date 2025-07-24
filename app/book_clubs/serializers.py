from rest_framework import serializers

from app.book_clubs.models import BookClub
from app.users.serializers import UserPreviewSerializer


class BookClubSerializer(serializers.ModelSerializer):
    owner = UserPreviewSerializer(read_only=True)
    members = UserPreviewSerializer(many=True, read_only=True)
    class Meta:
        model = BookClub
        fields = ('name', 'description', 'status', 'owner', 'members')


class CreateBookClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookClub
        fields = ('name', 'description')