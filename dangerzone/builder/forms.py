from builder.models import *
from django import forms
from django.forms import ModelForm
from django.forms import Textarea
import re

class mfProjectName(ModelForm):
	class Meta:
		model = ProjectName
	def clean(self):
		Project = self.cleaned_data.get('Project')
		projectTest = ProjectName.objects.filter(Project__iexact=Project)
		if projectTest:
			if not self._errors.has_key('Project'):
				from django.forms.util import ErrorList
				self._errors['Project'] = ErrorList()
			self._errors['Project'].append('Project name already exists.')
		else:
			pass
		return self.cleaned_data

def special_match(strg, search=re.compile(r'[^A-Za-z0-9_]').search):
	return not bool(search(strg))

class mfVariableDescription(ModelForm):
	class Meta:
		model = VariableDescription
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfVariableDescription, self).__init__(*args, **kwargs)
	def clean(self):
		VarName = self.cleaned_data.get('VarName')
		FieldType = self.cleaned_data.get('FieldType')
		VarMaxLength = self.cleaned_data.get('VarMaxLength')
		VarMaxDigits = self.cleaned_data.get('VarMaxDigits')
		VarMaxDecimalPlaces = self.cleaned_data.get('VarMaxDecimalPlaces')
		ProjectID = self.request.session['ProjectID']
		varTest = VariableDescription.objects.filter(ProjectID=ProjectID, VarName__iexact=VarName)
		if varTest:
			if not self._errors.has_key('VarName'):
				from django.forms.util import ErrorList
				self._errors['VarName'] = ErrorList()
			self._errors['VarName'].append('Variable name already exists.')
		else:
			pass
		if not special_match(VarName):
			if not self._errors.has_key('VarName'):
				from django.forms.util import ErrorList
				self._errors['VarName'] = ErrorList()
			self._errors['VarName'].append('Can only contain letters, numbers, and/or underscores.')
		else:
			pass
		if FieldType == "CharField":
			if not VarMaxLength:
				if not self._errors.has_key('VarMaxLength'):
					from django.forms.util import ErrorList
					self._errors['VarMaxLength'] = ErrorList()
				self._errors['VarMaxLength'].append('This field is required.')
			else:
				pass
		elif FieldType == "DecimalField":
			if not VarMaxDigits:
				if not self._errors.has_key('VarMaxDigits'):
					from django.forms.util import ErrorList
					self._errors['VarMaxDigits'] = ErrorList()
				self._errors['VarMaxDigits'].append('This field is required.')
			else:
				pass
			if not VarMaxDecimalPlaces:
				if not self._errors.has_key('VarMaxDecimalPlaces'):
					from django.forms.util import ErrorList
					self._errors['VarMaxDecimalPlaces'] = ErrorList()
				self._errors['VarMaxDecimalPlaces'].append('This field is required.')
			else:
				pass
		return self.cleaned_data

