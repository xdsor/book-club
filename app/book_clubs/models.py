from django.contrib.auth import get_user_model
from django.db import models

BOOK_CLUB_STATUSES = (
    ("IDLE", "IDLE"),
    ("VOTING", "VOTING"),
    ("WAIT_FOR_READING", "WAIT_FOR_READING"),
    ("READING", "READING")
)

user_model = get_user_model()

class BookClub(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    owner = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='owner_clubs')
    members = models.ManyToManyField(user_model, related_name='member_clubs')
    status = models.CharField(max_length=255, choices=BOOK_CLUB_STATUSES, default="IDLE")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<BookClub name={self.name} status={self.status}>'

class ScheduleObject(models.Model):
    planned_start_date = models.DateTimeField()
    start_date = models.DateTimeField(null=True)
    planned_finish_date = models.DateTimeField()
    finish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True