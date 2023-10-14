from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm


def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        return HttpResponse(f'Hi {first_name}!')
    context ={}
    context['form']= InputForm()
    return render(request, "appointments/index.html", context)