from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm


def index(request):
    context ={}
    context['form']= InputForm()
    return render(request, "appointments/index.html", context)