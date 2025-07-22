from django.contrib import admin

from app.book_clubs.reading_goal.models import BookClubReadingGoal


class BookClubReadingGoalAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookClubReadingGoal, BookClubReadingGoalAdmin)
