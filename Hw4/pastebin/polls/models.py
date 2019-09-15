from django.db import models
import datetime

class Paste(models.Model):
    text=models.TextField()
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField("Date", default=datetime.date.today)

    