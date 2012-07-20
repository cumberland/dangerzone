from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Textarea

FieldChoices = (
	("BigIntegerField", "BigIntegerField"),
	("BooleanField", "BooleanField"),
	("NullBooleanField", "NullBooleanField"),
	("CharField", "CharField"),
	("DateField", "DateField"),
	("DateTimeField", "DateTimeField"),
	("TimeField", "TimeField"),
	("DecimalField", "DecimalField"),
	("PositiveIntegerField", "PositiveIntegerField"),
	("TextField", "TextField"),
	("RadioButton", "RadioButton")
	)

class ProjectName(models.Model):
	Project = models.CharField(max_length=100, verbose_name="Project Name:")
	ProjectDescription = models.TextField(verbose_name="Project Description:")
	def __unicode__(self):
		return "%s" % self.Project

class VariableDescription(models.Model):
	ProjectID = models.ForeignKey(ProjectName, default=0, editable=False)
	VarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name
	VarName = models.CharField(max_length=62, verbose_name="Name of variable in the database:") # variable name
	VarDescription = models.CharField(max_length=500, verbose_name="Description of what the variable is collecting:") # description of variable purpose
	FieldType = models.CharField(max_length=20, choices=FieldChoices, verbose_name="Variable type:") # variable type
	VarBlank = models.BooleanField(verbose_name="Blank values are allowed.")
	VarNull = models.BooleanField(verbose_name="Null values are allowed.")
	VarMaxDigits = models.PositiveIntegerField(verbose_name="Maximum number of digits allowed (required):", blank=True, null=True)
	VarMaxDecimalPlaces = models.PositiveIntegerField(verbose_name="Maximum number of decimal places allowed (required):", blank=True, null=True)
	VarMaxLength = models.PositiveIntegerField(verbose_name="Maximum number of characters allowed (required):", blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.VarName

class AJAXTester(models.Model):
	AJAXVarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name

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

class mfVariableDescription(ModelForm):
	class Meta:
		model = VariableDescription
	def clean(self):
		VarName = self.cleaned_data.get('VarName')
		FieldType = self.cleaned_data.get('FieldType')
		VarMaxLength = self.cleaned_data.get('VarMaxLength')
		VarMaxDigits = self.cleaned_data.get('VarMaxDigits')
		VarMaxDecimalPlaces = self.cleaned_data.get('VarMaxDecimalPlaces')
		try:
			if " " in VarName:
				if not self._errors.has_key('VarName'):
					from django.forms.util import ErrorList
					self._errors['VarName'] = ErrorList()
				self._errors['VarName'].append('Cannot contain spaces.')
		except:
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




