from django.contrib import admin

from appAbuObaida.models import PrayerModel, QuestionModel, EventsModel


# Register your models here.
# @admin.register(PrayerModel)
# class PrayerModelAdmin(admin.ModelAdmin):
#     list_display = "__all__"
class PrayerModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.about_mosque = ("الصحابي الجليل وأحد المبشرين بالجنة أبو عبيدة بن الجراح"
                                " الذي أرسله النبي صلى الله عليه وسلم إلى نجران يعلم أهلها الإسلام والقرآن،"
                                " ويقضي بينهم بالقسط والميزان. قائد الجيوش الإسلامي، فاتح الديار الشامية، "
                                "وأمين الأمة المحمدية صاحب الإيمان القويم، والسلوك المستقيم، والقلب الرحيم،"
                                " والعقل الحكيم. أبو عبيدة بن الجراح هو أحد العشرة المبشرين بالجنة، حيث قال النبي: "
                                "“أبو بكر في الجنة، وعمر في الجنة، وعليّ في الجنة، وعثمان في الجنة، وطلحة في الجنة،"
                                " والزبير في الجنة، وعبد الرحمن بن عوف في الجنة، وسعد بن أبي وقاص في الجنة"
                                "، وسعيد بن زيد بن عمرو بن نفيل في الجنة، وأبو عبيدة بن الجراح في الجنة"
                                "”. معاهدة أبو عبيدة بن الجراح النبي أن ينفق حياته في سبيل الله "
                                "وأوفى بعهده وأبر بوعده. وهو من سكان الهجرتين، فقد هاجر إلى الحبشة،"
                                " في الهجرة الثانية، وهاجر من مكة إلى المدينة. وشهد غزوتي بدر وأحد وسائر الغزوات،"
                                " وواصل الجهاد بعد وفاة النبي صلى الله عليه وسلم مع أبي بكر وعمر رضي الله عنهما.")

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
