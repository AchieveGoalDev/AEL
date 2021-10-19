from django.shortcuts import render
from . import models


def unpack():
    questions = models.Question.objects.all()
    categories = models.QuestionCategory.objects.all()
    context = {'questions': questions, 'categories':categories}
    return context

def faq(request):
    return render(request, 'faq/faq.html', context = unpack())
