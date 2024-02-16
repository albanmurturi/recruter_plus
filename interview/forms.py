from django import forms

from .models import Interview
from subject.models import Subject

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('name', 'job_description', 'subjects',)

    name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-5 rounded-xl'})
        )
    job_description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Job Description',
        'class' : 'w-full py-4 px-6 rounded-xl border'
    }))
    subjects = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
        'placeholder': 'Subjects',
        'class': 'grid grid-cols-2 gap-4'
    }), queryset=Subject.objects.all())