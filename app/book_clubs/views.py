from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.book_clubs.models import BookClub
from app.book_clubs.serializers import BookClubSerializer, CreateBookClubSerializer


class BookClubsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = BookClub.objects.all()
        serializer = BookClubSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookClub.objects.get(id=pk)
        serializer = BookClubSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateBookClubSerializer(data=request.data)
        if serializer.is_valid():
            book_club = BookClub.objects.create(
                name=serializer.data['name'],
                description=serializer.data['description'],
                owner=request.user,
                status="IDLE"
            )
            book_club.members.add(request.user)
            book_club.save()
            return Response(BookClubSerializer(book_club).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        permission_classes = []
        if self.action not in ('list', 'retrieve'):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]