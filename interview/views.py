from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F

from subject.models import Question

from .models import Interview
from .forms import InterviewForm


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
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        # Extract data from the form
        if form.is_valid():
            name = form.cleaned_data['name']
            job_description = form.cleaned_data['job_description']
            subjects = form.cleaned_data['subjects']

            # Create a new object with the extracted data
            new_object = Interview.objects.create(
                name=name,
                job_description=job_description,
                user=request.user
            )
            new_object.subjects.set(subjects)

            new_object.save()
            return redirect('/interview')
    else:
         form = InterviewForm()

    return render(request, 'interview/new_interview.html', {'form':  form} )