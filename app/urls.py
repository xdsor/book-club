from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers

from app.book_clubs.views import BookClubsViewSet
from app.users.views import self_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/self-info', self_user_info),
    path('api/logout', LogoutView.as_view()),
    path('api/auth/', include('social_django.urls', namespace="social")),
]

router = routers.SimpleRouter()
router.register(r'api/book-clubs', BookClubsViewSet, basename='book-clubs')

urlpatterns += router.urls