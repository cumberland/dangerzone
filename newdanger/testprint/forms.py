from doubt.models import *
from doubt.options import *
from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from django.forms.util import ErrorList
import re


class mfNewPatient(ModelForm):
	class Meta:
		model = NewPatient
		widgets = {
		'Gender': RadioSelect(choices=NewPatient_Gender),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfNewPatient, self).__init__(*args, **kwargs)


class mfFollowUp24H(ModelForm):
	class Meta:
		model = FollowUp24H
		widgets = {
		'FocalResolved': RadioSelect(choices=FollowUp24H_FocalResolved),
		'AllSymptomsResolved': RadioSelect(choices=FollowUp24H_AllSymptomsResolved),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfFollowUp24H, self).__init__(*args, **kwargs)


class mfFirstEvent(ModelForm):
	class Meta:
		model = FirstEvent
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfFirstEvent, self).__init__(*args, **kwargs)


class mfCT(ModelForm):
	class Meta:
		model = CT
		widgets = {
		'PlainCTInfarct': RadioSelect(choices=CT_PlainCTInfarct),
		'PlainCTLesion': RadioSelect(choices=CT_PlainCTLesion),
		'PlainCTSide': RadioSelect(choices=CT_PlainCTSide),
		'OldInfarct': RadioSelect(choices=CT_OldInfarct),
		'OldInfarctLesion': RadioSelect(choices=CT_OldInfarctLesion),
		'OldInfarctSide': RadioSelect(choices=CT_OldInfarctSide),
		'CTASI': RadioSelect(choices=CT_CTASI),
		'CTANeck': RadioSelect(choices=CT_CTANeck),
		'AorticArch': RadioSelect(choices=CT_AorticArch),
		'GreatVesselOrigin': RadioSelect(choices=CT_GreatVesselOrigin),
		'CTAWillis': RadioSelect(choices=CT_CTAWillis),
		'CTASIVisibleAcute': RadioSelect(choices=CT_CTASIVisibleAcute),
		'CTASIVisibleOld': RadioSelect(choices=CT_CTASIVisibleOld),
		'CTASIVisibleNoInfarct': RadioSelect(choices=CT_CTASIVisibleNoInfarct),
		'WhiteMatterChangeRating': RadioSelect(choices=CT_WhiteMatterChangeRating),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfCT, self).__init__(*args, **kwargs)


class mfMRI(ModelForm):
	class Meta:
		model = MRI
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfMRI, self).__init__(*args, **kwargs)


class mfDoppler(ModelForm):
	class Meta:
		model = Doppler
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfDoppler, self).__init__(*args, **kwargs)


class mfFollowUp(ModelForm):
	class Meta:
		model = FollowUp
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfFollowUp, self).__init__(*args, **kwargs)


class mfStrokeOutcome(ModelForm):
	class Meta:
		model = StrokeOutcome
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfStrokeOutcome, self).__init__(*args, **kwargs)


class mfFinalDiagnosis(ModelForm):
	class Meta:
		model = FinalDiagnosis
		widgets = {}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfFinalDiagnosis, self).__init__(*args, **kwargs)


class mfBaseline(ModelForm):
	class Meta:
		model = Baseline
		widgets = {
		'ReferFrom': RadioSelect(choices=Baseline_ReferFrom),
		'StrokeAssessFrom': RadioSelect(choices=Baseline_StrokeAssessFrom),
		'PatientLocation': RadioSelect(choices=Baseline_PatientLocation),
		'MRIType': RadioSelect(choices=Baseline_MRIType),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfBaseline, self).__init__(*args, **kwargs)


class mfPlainCTVasc(ModelForm):
	class Meta:
		model = PlainCTVasc
		widgets = {
		'PlainCTVascTerritory': RadioSelect(choices=PlainCTVasc_PlainCTVascTerritory),
		'PlainCTVascSide': RadioSelect(choices=PlainCTVasc_PlainCTVascSide),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfPlainCTVasc, self).__init__(*args, **kwargs)


class mfCTAWillisVasc(ModelForm):
	class Meta:
		model = CTAWillisVasc
		widgets = {
		'CTAWillisVascSide': RadioSelect(choices=CTAWillisVasc_CTAWillisVascSide),
		'CTAWillisVascSite': RadioSelect(choices=CTAWillisVasc_CTAWillisVascSite),
		'CTAWillisVascStenosis': RadioSelect(choices=CTAWillisVasc_CTAWillisVascStenosis),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfCTAWillisVasc, self).__init__(*args, **kwargs)


class mfOldInfarctVasc(ModelForm):
	class Meta:
		model = OldInfarctVasc
		widgets = {
		'OldInfarctVascTerritory': RadioSelect(choices=OldInfarctVasc_OldInfarctVascTerritory),
		'OldInfarctVascSide': RadioSelect(choices=OldInfarctVasc_OldInfarctVascSide),}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfOldInfarctVasc, self).__init__(*args, **kwargs)

