import random
from datetime import datetime
from typing import Tuple

import vestaboard
from django.http import HttpResponse
from django.shortcuts import render

from . import ENV
from .forms import PatientNameForm
from .models import AppointmentPosts
from .words import ADJECTIVES, BODY_PARTS, PROCEDURES


def _get_proc_body_adj() -> Tuple:
    return (
        random.choice(ADJECTIVES),
        random.choice(BODY_PARTS),
        random.choice(PROCEDURES),
    )


def post_appointment(patient_name: str) -> Tuple:
    installation = vestaboard.Installable(
        ENV["KEY"], ENV["SECRET"], saveCredentials=False
    )
    board = vestaboard.Board(installation)
    now = datetime.now()
    date = now.strftime("%m.%d.%Y")
    time = now.strftime("%I:%M%p")
    procedure = _get_proc_body_adj()
    appointment = f"EMERGENCY PROCEDURES\n{date} {time}\n\nPATIENT: {patient_name}\n{procedure[0]} {procedure[1]}\n{procedure[2]}"
    board.post(appointment)
    return appointment


def insert_appointment_post(appointment: str):
    row = AppointmentPosts(appointment=appointment)
    row.save()
    return row


def index(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        if not patient_name:
            return HttpResponse('Please enter your name and press "Submit"...and we will make you submit.')

        appointment = post_appointment(patient_name)
        if not appointment:
            return HttpResponse(f'FAILED to schedule an appointment for {patient_name}.')

        delta = AppointmentPosts.latest_post_time_delta()
        print(f"DELTA: {delta}")
        insert_appointment_post(appointment)
        return HttpResponse(f'Successfully scheduled an appointment: {appointment}.')
    context ={}
    context['form']= PatientNameForm()
    return render(request, "appointments/index.html", context)