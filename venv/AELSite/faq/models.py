from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField

class QuestionCategory(models.Model):
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural='Question Categories'

    category = models.CharField(max_length=10)
    
class Question(models.Model):
    def __str__(self):
        return self.question
    
    question_category = models.ForeignKey(QuestionCategory, on_delete=SET_NULL, null=True)
    question = models.CharField(max_length=25)
    answer = models.TextField()