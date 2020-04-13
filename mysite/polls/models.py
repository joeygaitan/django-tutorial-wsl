import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    def __init__(self):
        self.question_text = models.CharField(max_length=200)
        self.pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 


class Choice(models.Model):
    def __init__(self):
        self.question = models.ForeignKey(Question, on_delete=models.CASCADE)
        self.choice_text = models.CharField(max_length=200)
        self.votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text