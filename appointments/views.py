from django.http import HttpResponse
from django.shortcuts import render

from .forms import PatientNameForm


def index(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        if not patient_name:
            return HttpResponse('Please enter your name and press "Submit"...and we will make you submit.')
        return HttpResponse(f'Successfully scheduled an appointment for {patient_name}.') 
    context ={}
    context['form']= PatientNameForm()
    return render(request, "appointments/index.html", context)