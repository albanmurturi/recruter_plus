from django.shortcuts import render, get_object_or_404
from interview.models import Interview
from django.db.models import Prefetch

# Create your views here.
def index(request):
    interviews = Interview.objects.all()
    print("interviews", interviews)
    return render(request, 'interview/interview.html', {
        'interviews': interviews
    })

def interview_detail(request, id):
    # Fetch the interview by id and render a detail template
    interview = get_object_or_404(Interview, id=id)

    # Prefetch subjects and their related questions
    subjects_with_questions = interview.subjects.prefetch_related(
        Prefetch('questions')
    ).all()

    # Prepare the context for rendering
    context = {
        'interview': interview,
        'subjects': subjects_with_questions,
    }
    return render(request, 'interview/interview_detail.html', context)