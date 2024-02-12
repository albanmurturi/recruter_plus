from django.shortcuts import render, get_object_or_404
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

def subject_detail(request, id):
    # Fetch the subject by id and render a detail template
    subject_detail = get_object_or_404(Subject.objects.prefetch_related('questions'), id=id)
    return render(request, 'subject_detail.html', {'subject_detail': subject_detail})