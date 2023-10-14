from django.http import JsonResponse
from django.shortcuts import render

from .forms import InputForm


def index(request):
    context ={}
    context['form']= InputForm()
    if request.method == 'POST':
        return JsonResponse({'message': 'Hello, world!'})
    return render(request, "appointments/index.html", context)