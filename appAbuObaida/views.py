from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.translation import activate

from appAbuObaida.models import PrayerModel, QuestionModel, EventsModel


def index(request):
    activate('ar')
    prayer_model = PrayerModel.objects.all()
    all_events = EventsModel.objects.all()
    context = {
        'prayer_model': prayer_model,
        'all_events': all_events
    }
    return render(request, 'appAbuObaida/index.html', context)


def questions_blog(request):
    activate('ar')
    questions = QuestionModel.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'appAbuObaida/questions_blog.html', context)


def question_detail(request, pk):
    activate('ar')
    question_detailed = get_object_or_404(QuestionModel, pk=pk)
    context = {
        'question_detailed': question_detailed
    }
    return render(request, 'appAbuObaida/question_detail.html', context)


def events_view(request):
    activate('ar')
    events = EventsModel.objects.all()
    context = {
        'events': events
    }
    return render(request, 'appAbuObaida/events.html', context)


def events_details(request, event_id):
    activate('ar')

    event_to_detailed = get_object_or_404(EventsModel, pk=event_id)
    context = {
        'event_to_detailed': event_to_detailed
    }
    return render(request, 'appAbuObaida/event_details.html', context)


def about(request):
    activate('ar')

    about_the_mosque = PrayerModel.objects.all()
    context = {
        'about_the_mosque': about_the_mosque
    }
    return render(request, 'appAbuObaida/about.html', context)


def contact_us(request):
    return render(request, 'appAbuObaida/contact_us.html')


def search_question(request):
    question_detailed = request.GET.get('search')
    items_found = None

    if question_detailed != "":
        print("Searching for question " + question_detailed)
        items_found = QuestionModel.objects.filter(Q(question_title__icontains=question_detailed))
        if items_found.exists():
            print("The item exists")
            # logger.info("Item exists in the database!")
        else:
            print("The item does not exist")
            # logger.warning("Item doesn't exist in the database.")
    else:
        print("No questions asked!")
        # logger.warning("No search item provided")

    # recipe = get_object_or_404(Recipe, id=id)
    context = {
        "items_found": items_found,
    }

    return render(request, 'appAbuObaida/search_results.html', context)
