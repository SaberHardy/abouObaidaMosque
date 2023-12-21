from django.contrib import admin

from appAbuObaida.models import PrayerModel, QuestionModel

# Register your models here.
# @admin.register(PrayerModel)
# class PrayerModelAdmin(admin.ModelAdmin):
#     list_display = "__all__"

admin.site.register(PrayerModel)
admin.site.register(QuestionModel)
