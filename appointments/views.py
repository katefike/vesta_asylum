from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm


def index(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        return HttpResponse(f'Hi {patient_name}!')
    context ={}
    context['form']= InputForm()
    return render(request, "appointments/index.html", context)