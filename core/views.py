from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.db.models import Count

from subject.models import Subject

from .decorators import redirect_if_authenticated
from .forms import SignupForm, LoginForm

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

@redirect_if_authenticated
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


@method_decorator(redirect_if_authenticated, name='dispatch')
class CustomLoginView(auth_views.LoginView):
    # Optionally, you can customize template_name or any other properties of LoginView here
    form_class = LoginForm
    template_name = 'core/login.html'