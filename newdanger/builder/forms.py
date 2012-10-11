from builder.models import *
from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from django.forms.util import ErrorList
import re
from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet

class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(BaseAuthorFormSet, self).__init__(*args, **kwargs)
        

def special_match(strg, search=re.compile(r'[^A-Za-z0-9_]').search):
	return not bool(search(strg))

class mfProject(ModelForm):
	class Meta:
		model = Project
	def clean(self):
		ProjectName = self.cleaned_data.get('ProjectName')
		if ProjectName:
			projectTest = Project.objects.filter(ProjectName__iexact=ProjectName)
			if projectTest:
				if not self._errors.has_key('ProjectName'):
					self._errors['ProjectName'] = ErrorList()
				self._errors['ProjectName'].append('Project name already exists.')
			else:
				pass
		return self.cleaned_data


class mfForm(ModelForm):
	class Meta:
		model = Form
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfForm, self).__init__(*args, **kwargs)
	def clean(self):
		FormName = self.cleaned_data.get('FormName')
		ProjectID = self.request.session['ProjectID']
		if FormName:
			formTest = Form.objects.filter(ProjectID=ProjectID, FormName__iexact=FormName)
			if formTest:
				if not self._errors.has_key('FormName'):
					self._errors['FormName'] = ErrorList()
				self._errors['FormName'].append('Form name already exists.')
			else:
				pass
			if not special_match(FormName):
				if not self._errors.has_key('FormName'):
					self._errors['FormName'] = ErrorList()
				self._errors['FormName'].append('Can only contain letters, numbers, and/or underscores.')
		return self.cleaned_data
	def save(self, force_insert=False, force_update=False, commit=True):
		m = super(mfForm, self).save(commit=False)
		m.ProjectID = self.request.session['ProjectID']
		if commit:
			m.save()
		return m


class mfVariable(ModelForm):
	class Meta:
		model = Variable
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mfVariable, self).__init__(*args, **kwargs)
	def clean(self):
		VarName = self.cleaned_data.get('VarName')
		FieldType = self.cleaned_data.get('FieldType')
		VarMaxLength = self.cleaned_data.get('VarMaxLength')
		VarMaxDigits = self.cleaned_data.get('VarMaxDigits')
		VarMaxDecimalPlaces = self.cleaned_data.get('VarMaxDecimalPlaces')
		FormID = self.request.session['FormID']
		if VarName:
			if self.instance:
				if self.instance.VarName == VarName:
					pass
				else:
					varTest = Variable.objects.filter(FormID=FormID, VarName__iexact=VarName)
					if varTest:
						if not self._errors.has_key('VarName'):
							self._errors['VarName'] = ErrorList()
						self._errors['VarName'].append('Variable name already exists.')
					else:
						pass
			if not special_match(VarName):
				if not self._errors.has_key('VarName'):
					self._errors['VarName'] = ErrorList()
				self._errors['VarName'].append('Can only contain letters, numbers, and/or underscores.')
			else:
				pass
		if FieldType == "CharField":
			if not VarMaxLength:
				if not self._errors.has_key('VarMaxLength'):
					self._errors['VarMaxLength'] = ErrorList()
				self._errors['VarMaxLength'].append('This field is required.')
			else:
				pass
		elif FieldType == "DecimalField":
			if not VarMaxDigits:
				if not self._errors.has_key('VarMaxDigits'):
					self._errors['VarMaxDigits'] = ErrorList()
				self._errors['VarMaxDigits'].append('This field is required.')
			else:
				pass
			if not VarMaxDecimalPlaces:
				if not self._errors.has_key('VarMaxDecimalPlaces'):
					self._errors['VarMaxDecimalPlaces'] = ErrorList()
				self._errors['VarMaxDecimalPlaces'].append('This field is required.')
			else:
				pass
			if VarMaxDigits and VarMaxDecimalPlaces:
				if int(VarMaxDigits) < int(VarMaxDecimalPlaces):
					if not self._errors.has_key('VarMaxDigits'):
						self._errors['VarMaxDigits'] = ErrorList()
					self._errors['VarMaxDigits'].append('Max digits must be greater than max decimal places.')
			else:
				pass
		return self.cleaned_data
	def save(self, force_insert=False, force_update=False, commit=True):
		m = super(mfVariable, self).save(commit=False)
		m.FormID = self.request.session['FormID']
		if commit:
			m.save()
		else:
			pass
		return m







