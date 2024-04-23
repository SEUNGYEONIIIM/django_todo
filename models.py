from django.db import models
from datetime import date
import datetime

# Create your models here.


class TodoList(models.Model):
    name = models.CharField( verbose_name="투두 리스트")
    text = models.TextField( verbose_name="내용")
    start_day = models.DateField( verbose_name="시작 날짜")
    date = models.DateField(verbose_name="기한")
    
    def remaining_days(self):
        dday = self.date - date.today()
        days = dday.days 
        return days

    def __str__(self):
        return f'{self.name} | {self.text} | {self.start_day} | {self.date}'



