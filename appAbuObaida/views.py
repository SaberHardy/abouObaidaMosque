from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'appAbuObaida/index.html')


def questions_blog(request):
    return render(request, 'appAbuObaida/questions_blog.html')


def question_detail(request):
    # question_detailed = get_object_or_404(Model, pk=question_detail)
    context = {
        # question_detailed: 'question_detailed'
    }
    return render(request, 'appAbuObaida/question_detail.html', context)
