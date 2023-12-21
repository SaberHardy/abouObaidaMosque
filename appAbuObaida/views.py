from django.shortcuts import render
from django.utils.translation import activate

from appAbuObaida.models import PrayerModel, QuestionModel


def index(request):
    # activate('ar')
    prayer_model = PrayerModel.objects.all()
    context = {
        'prayer_model': prayer_model
    }
    return render(request, 'appAbuObaida/index.html', context)


def questions_blog(request):
    questions = QuestionModel.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'appAbuObaida/questions_blog.html', context)


def question_detail(request):
    # question_detailed = get_object_or_404(Model, pk=question_detail)
    context = {
        # question_detailed: 'question_detailed'
    }
    return render(request, 'appAbuObaida/question_detail.html', context)


def events(request):
    return render(request, 'appAbuObaida/events.html')


def about(request):
    return render(request, 'appAbuObaida/about.html')


def contact_us(request):
    return render(request, 'appAbuObaida/contact_us.html')
