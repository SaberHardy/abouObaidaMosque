from django.contrib import admin

from appAbuObaida.models import PrayerModel, QuestionModel, EventsModel


# Register your models here.
# @admin.register(PrayerModel)
# class PrayerModelAdmin(admin.ModelAdmin):
#     list_display = "__all__"
class PrayerModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.about_mosque = "Your default about_mosque value"

        existing_instance = PrayerModel.objects.filter(id=obj.id, image__isnull=False).first()
        if existing_instance:
            # Delete the old image file
            existing_instance.image.delete()

        obj.save()

    def has_add_permission(self, request):
        # Check if there are any existing instances of PrayerModel
        existing_count = PrayerModel.objects.count()

        # If there are already instances, return False to disable the "Add" button
        return existing_count == 0


admin.site.register(PrayerModel, PrayerModelAdmin)
admin.site.register(QuestionModel)
admin.site.register(EventsModel)
