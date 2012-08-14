from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import Textarea
import re
import reversion




FieldChoices = (
	("BigIntegerField", "Integer"),
	("PositiveIntegerField", "Positive Integer"),
	("DecimalField", "Decimal"),
	("BooleanField", "Checkbox"),
	("RadioButton", "Radio Button"),
	("CharField", "Text"),
	("TextField", "Text Area"),
	("DateField", "Date"),
	("TimeField", "Time"),
	("DateTimeField", "DateTime")
	)

class Audit(models.Model):
	record = models.BigIntegerField(default=1, editable=False )
	datetime = models.DateTimeField(auto_now_add=True)
	user = models.CharField(max_length=50, editable=False)
	class Meta:
		abstract = True

class ProjectName(Audit):
	Project = models.CharField(max_length=100, verbose_name="Project Name:")
	ProjectDescription = models.TextField(verbose_name="Project Description:")
	def __unicode__(self):
		return "%s" % self.Project
	class Meta:
		get_latest_by = 'record'

class VariableDescription(Audit):
	ProjectID = models.ForeignKey(ProjectName, default=0, editable=False)
	VarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name
	VarName = models.CharField(max_length=62, verbose_name="Name of variable in the database:") # variable name
	VarDescription = models.CharField(max_length=500, verbose_name="Description of what the variable is collecting:") # description of variable purpose
	FieldType = models.CharField(max_length=20, choices=FieldChoices, verbose_name="Variable type:") # variable type
	VarBlank = models.BooleanField(verbose_name="Blank values are allowed.")
	VarNull = models.BooleanField(verbose_name="Null values are allowed.")
	Identifier = models.BooleanField(verbose_name="Collects identifiable information.")
	VarMaxDigits = models.PositiveIntegerField(verbose_name="Maximum number of digits allowed (required):", blank=True, null=True)
	VarMaxDecimalPlaces = models.PositiveIntegerField(verbose_name="Maximum number of decimal places allowed (required):", blank=True, null=True)
	VarMaxLength = models.PositiveIntegerField(verbose_name="Maximum number of characters allowed (required):", blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.VarName
	class Meta:
		get_latest_by = 'record'

class AJAXTester(models.Model):
	AJAXVarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name

reversion.register(ProjectName)

class Options(Audit):
	ProjectID = models.ForeignKey(ProjectName, default=0, editable=False)
	VarID = models.ForeignKey(VariableDescription, default=0, editable=False)
	Label = models.CharField(max_length=500)
	Value = models.BigIntegerField()
