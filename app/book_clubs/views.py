from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.book_clubs.models import BookClub
from app.book_clubs.serializers import BookClubSerializer, CreateBookClubSerializer

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 50
    page_size_query_param = 'page_size'

class BookClubsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = BookClub.objects.all()

        paginator = MyPageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)

        serializer = BookClubSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

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