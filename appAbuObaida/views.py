from django.shortcuts import render, get_object_or_404
from django.utils.translation import activate

from appAbuObaida.models import PrayerModel, QuestionModel, EventsModel


def index(request):
    # activate('ar')
    prayer_model = PrayerModel.objects.all()
    all_events = EventsModel.objects.all()
    context = {
        'prayer_model': prayer_model,
        'all_events': all_events
    }
    return render(request, 'appAbuObaida/index.html', context)


def questions_blog(request):
    questions = QuestionModel.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'appAbuObaida/questions_blog.html', context)


def question_detail(request, pk):
    question_detailed = get_object_or_404(QuestionModel, pk=pk)
    context = {
        'question_detailed': question_detailed
    }
    return render(request, 'appAbuObaida/question_detail.html', context)


def events_view(request):
    events = EventsModel.objects.all()
    context = {
        'events': events
    }
    return render(request, 'appAbuObaida/events.html', context)


def events_details(request, event_id):
    event_to_detailed = get_object_or_404(EventsModel, pk=event_id)
    context = {
        'event_to_detailed': event_to_detailed
    }
    return render(request, 'appAbuObaida/event_details.html', context)


def about(request):
    return render(request, 'appAbuObaida/about.html')


def contact_us(request):
    return render(request, 'appAbuObaida/contact_us.html')
