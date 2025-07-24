from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.book_clubs.views import BookClubsViewSet
from app.users.views import self_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('self-info', self_user_info)
]

router = routers.SimpleRouter()
router.register(r'book-clubs', BookClubsViewSet, basename='book-clubs')

urlpatterns += router.urls