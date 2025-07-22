from django.contrib import admin

from app.book_clubs.models import BookClub


class BookClubAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookClub, BookClubAdmin)
