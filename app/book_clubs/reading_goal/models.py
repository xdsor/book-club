from django.db import models

from app.book_clubs.models import ScheduleObject
from app.book_clubs.reading.models import BookClubReading


class BookClubReadingGoal(ScheduleObject):
    book_club_reading = models.ForeignKey(BookClubReading, on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    target_percent = models.PositiveSmallIntegerField(default=0)
