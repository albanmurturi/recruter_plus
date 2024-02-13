from django.shortcuts import render, get_object_or_404, redirect
from subject.models import Subject
from django.db.models import Count
from .forms import SignupForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    subjects_with_question_count = Subject.objects.annotate(
        question_num=Count('questions')
    ).values(
        'id', 'name', 'description', 'question_num'
    )
    return render(request, 'core/index.html', {
        'subjects': subjects_with_question_count
    })

def subject_detail(request, id):
    # Fetch the subject by id and render a detail template
    subject_detail = get_object_or_404(Subject.objects.prefetch_related('questions'), id=id)
    return render(request, 'core/subject_detail.html', {'subject_detail': subject_detail})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('core:index')