from django import forms


class PatientNameForm(forms.Form):

	patient_name = forms.CharField(max_length = 13)