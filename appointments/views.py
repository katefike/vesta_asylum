import random
from datetime import datetime, timedelta
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
        delta = AppointmentPosts.latest_post_time_delta()
        NEW_SUBMISSION_WAIT_SEC = int(ENV["NEW_SUBMISSION_WAIT_SEC"])
        if delta < timedelta(seconds=NEW_SUBMISSION_WAIT_SEC):
            remaining_time = timedelta(seconds=NEW_SUBMISSION_WAIT_SEC) - delta
            remaining_seconds = int(remaining_time.total_seconds())
            return HttpResponse(f'An appointment stays on the board for {NEW_SUBMISSION_WAIT_SEC} seconds. Re-submit in {remaining_seconds} seconds.')

        patient_name = request.POST['patient_name']
        if not patient_name:
            return HttpResponse('Enter your name and press "Submit"...and we will make you submit.')

        appointment = post_appointment(patient_name)

        if not appointment:
            return HttpResponse(f'FAILED to schedule an appointment for {patient_name}.')

        insert_appointment_post(appointment)
        return HttpResponse(f'Successfully scheduled an appointment: {appointment}.')
    context ={}
    context['form']= PatientNameForm()
    return render(request, "appointments/index.html", context)