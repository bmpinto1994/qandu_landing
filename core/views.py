from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('success')
class Success(TemplateView):
  template_name = "success.html"