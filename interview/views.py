from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from django.db.models import F

from subject.models import Subject

from interview.models import Interview
from subject.models import Question


# Create your views here.
@login_required
def interview(request):
    user = request.user
    interviews = Interview.objects.filter(user=user)
    print("interviews", interviews)
    return render(request, 'interview/interview.html', {
        'interviews': interviews
    })
    
@login_required
def interview_detail(request, id):

    user = request.user
    interviews = Interview.objects.filter(user=user)

    # Fetch the interview by id and render a detail template
    interview = get_object_or_404(interviews, id=id)

    # Annotate a random question with its subject
    random_question = Question.objects.filter(subject__in=interview.subjects.all()).annotate(
        subject__id=F('subject_id'),
        subject_name=F('subject__name'),
        subject_description=F('subject__description'),
        question_id=F('id'),
        question_text=F('text'),
        question_answer=F('answer'),
    ).order_by('?').first()


    # Prepare the context for rendering
    context = {
        'interview': interview,
        'subject_with_random_question': random_question,
    }
    return render(request, 'interview/interview_detail.html', context)

def new_interview(request):
    subjects = Subject.objects.all()
    return render(request, 'interview/new_interview.html', {'subjects': subjects } )