from django.db import models
from django.template.defaultfilters import date
import locale
from django.utils import formats
from django.utils.translation import activate


class PrayerModel(models.Model):
    month_field = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='static/imgs')
    about_mosque = models.TextField(blank=True, null=True)

    # class Meta:
    #     verbose_name = "الصلاة"
    #     verbose_name_plural = "الصلاة"

    # def __str__(self):
    #     activate('ar')
    #     locale.setlocale(locale.LC_TIME, 'ar')
    #
    #     formatted_date = formats.date_format(self.month_field, format='d F Y ')
    #
    #     locale.setlocale(locale.LC_TIME, '')
    #
    #     return f"تم إنشاؤه يوم: {formatted_date}"

    def __str__(self):
        return formats.date_format(self.month_field, format='d F Y ')


class QuestionModel(models.Model):
    question_title = models.CharField(max_length=500)
    question_answer = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_title


class EventsModel(models.Model):
    event_title = models.CharField(max_length=500)
    event_description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.event_title
