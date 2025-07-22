from django.contrib import admin

from app.books.models import Book, BookAuthor


class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
