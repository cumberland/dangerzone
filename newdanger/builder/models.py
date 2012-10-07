from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import reversion

from django.core.signals import request_finished,request_started

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
	("DateTimeField", "DateTime"),
	("EmailField", "Email")
	)

class Project(models.Model):
	ProjectName = models.CharField(max_length=100, verbose_name="Project Name:")
	ProjectURL = models.SlugField(max_length=18, verbose_name="Project URL:")
	ProjectDescription = models.TextField(verbose_name="Project Description:")
	def __unicode__(self):
		return "%s" % self.ProjectName

class Form(models.Model):
	ProjectID = models.ForeignKey(Project, default=0, editable=False, related_name="Form")
	FormName = models.CharField(verbose_name="Form Name:", max_length=40)
	FormDescription = models.TextField(verbose_name="Form Description:")
	VariableOrder = models.CommaSeparatedIntegerField(max_length=500, default="[]", editable=False, blank=True)
	def __unicode__(self):
		return "%s" % (self.FormName)

class Variable(models.Model):
	FormID = models.ForeignKey(Form, default=0, editable=False, related_name="Variable")
	VarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name
	VarName = models.CharField(max_length=32, verbose_name="Name of variable in the database:") # variable name
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

class Option(models.Model):
	VariableID = models.ForeignKey(Variable, default=0, editable=False, related_name="Option")
	Value = models.BigIntegerField()
	Label = models.CharField(max_length=1000)
	def __unicode__(self):
		return "%s, %s" % (self.Value, self.Label)

def print_keyword_args(**kwargs):
# kwargs is a dict of the keyword args passed to the function
	for key, value in kwargs.iteritems():
		print "%s = %s" % (key, value)


@receiver(reversion.pre_revision_commit)
def it_worked(sender, **kwargs):
	# print "Got the signal."
	currentVersion = kwargs.pop('versions')[0].field_dict
	try:
		pastVersion = reversion.get_for_object(kwargs.pop('instances')[0])[0].field_dict
	except IndexError:
		comment = "Created."
	except TypeError:
		comment = "Deleted."
	else:
		changes = set(currentVersion.items()) - set(pastVersion.items())
		changedVars = []
		for var in changes:
			changedVars.append(var[0])
		comment = "Changed: %s" % ", ".join(changedVars)
	revision = kwargs.pop('revision')
	revision.comment = comment
	revision.save()
	kwargs['revision'] = revision
	# print dir(sender.get_for_object)
	# print dir(sender)
	sender.save_revision
	# print_keyword_args(**kwargs)
	# print dir(kwargs.pop('instances'))
	# print dir(kwargs.pop('revision'))
	# for i in kwargs.pop('instances'):
	# 	print dir(i)
	# 	print dir(i.clean_fields)



@receiver(request_started)
def my_callback(sender, **kwargs):
    print "#####--SENDER--#####"
    print dir(sender)
    print "#####--SIGNAL--#####"
    print kwargs.pop('signal')
    print kwargs


