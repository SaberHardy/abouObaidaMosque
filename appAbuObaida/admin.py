from django.contrib import admin

from appAbuObaida.models import PrayerModel


# Register your models here.
# @admin.register(PrayerModel)
# class PrayerModelAdmin(admin.ModelAdmin):
#     list_display = "__all__"

admin.site.register(PrayerModel)
