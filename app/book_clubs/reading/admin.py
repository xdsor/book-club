from django.contrib import admin

from app.book_clubs.reading.models import BookClubReading


class BookClubReadingAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookClubReading, BookClubReadingAdmin)
