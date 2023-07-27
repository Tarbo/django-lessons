from django.db import models


# Create your models here.
class Meeting(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=255)
    meeting_agenda = models.TextField()
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.meeting_title} at {self.meeting_location} on {self.meeting_date} at {self.meeting_time}'

    class Meta:
        """
            A class to represent the meta data of the Meetings model.
        """
        db_table = 'meeting'
        verbose_name_plural = 'meeting'
        ordering = ['meeting_date']


class Room(models.Model):
    room_name = models.CharField(max_length=255)
    room_capacity = models.IntegerField(default=2)
    floor_number = models.IntegerField(default=0)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.room_name} at {self.floor_number} floor with a room number {self.room_number} has capacity of ' \
               f'{self.room_capacity}'

    class Meta:
        """
            A class to represent the meta data of the Rooms model.
        """
        db_table = 'room'
        verbose_name_plural = 'room'
        ordering = ['room_name']
