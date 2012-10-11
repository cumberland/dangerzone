from cep.models import *
from cep.options import *
from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from django.forms.util import ErrorList
import re


class mfNewPatient(ModelForm):
	class Meta:
		model = NewPatient
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfNewPatient, self).__init__(*args, **kwargs)


class mfConsent(ModelForm):
	class Meta:
		model = Consent
		widgets = {
		'ChartReview': RadioSelect(choices=Consent_ChartReview),
		'BioSamples': RadioSelect(choices=Consent_BioSamples),
		'ResearchContact': RadioSelect(choices=Consent_ResearchContact),
		'PatientSigned': RadioSelect(choices=Consent_PatientSigned),
		'WitnessSigned': RadioSelect(choices=Consent_WitnessSigned),
		'ProxyConsent': RadioSelect(choices=Consent_ProxyConsent),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfConsent, self).__init__(*args, **kwargs)



