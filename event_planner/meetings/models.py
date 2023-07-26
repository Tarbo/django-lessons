from django.db import models


# Create your models here.
class Meetings(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=255)
    meeting_agenda = models.TextField()

    def __str__(self):
        return self.meeting_title

    class Meta:
        """
            A class to represent the meta data of the Meetings model.
        """
        db_table = 'meetings'
        verbose_name_plural = 'meetings'
        ordering = ['meeting_date']
