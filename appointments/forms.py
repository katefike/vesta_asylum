from django import forms


class InputForm(forms.Form):

	patient_name = forms.CharField(max_length = 13)