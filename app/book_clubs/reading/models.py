from django.db import models

from app.book_clubs.models import BookClub, ScheduleObject
from app.books.models import Book

BOOK_CLUB_READING_STATUSES = (
    ("WAITING_FOR_START", "WAITING_FOR_START"),
    ("STARTED", "STARTED"),
    ("DONE", "DONE"),
    ("CANCELLED", "CANCELLED")
)

class BookClubReading(ScheduleObject):
    book_club = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=BOOK_CLUB_READING_STATUSES, default="WAITING_FOR_START")