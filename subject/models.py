from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()


    def __str__(self):
        return self.question
