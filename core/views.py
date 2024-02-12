from django.shortcuts import render
from subject.models import Subject, Question
from django.db.models import Count

# Create your views here.
def index(request):
    subjects_with_question_count = Subject.objects.annotate(
        question_num=Count('questions')
    ).values(
        'id', 'name', 'description', 'question_num'
    )
    return render(request, 'index.html', {
        'subjects': subjects_with_question_count
    })