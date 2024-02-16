from django.db import models
from subject.models import Subject, Question
from django.contrib.auth.models import User

# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length=255)
    job_description = models.TextField()
    subjects = models.ManyToManyField(Subject)
    learend_quesitons = models.ManyToManyField(Question)
    user = models.ForeignKey(User, related_name="created_interview", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

