from builder.models import Option
import re

# Outine Process
# Startapp - 1) Create folder with slug name 2) __init__.py the folder 3) Create the files that will be used
# i) admin.py - DONE
# ii) forms.py - DONE
# iii) models.py - DONE
# iv) urls.py - 
# v) choices.py - DONE
# vi) views.py - 

def writeModels(Project):
	newModels = open("../newdanger/stroke/doubt/models.py", "w+")
	modelWriter = open("../newdanger/stroke/doubt/models.py", "a")
	modelWriter.write(
"""from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import reversion""")
	for form in Project:
		VariableWrite = []
		for variable in form.Variable.all():
			modeldetails = "verbose_name='%s'" % re.sub("'", "\\'", variable.VarLabel.strip())
			if variable.FieldType != "BooleanField":
				modeldetails = "%s, blank=%s, null=%s" % (modeldetails, variable.VarBlank, variable.VarNull)
			else:
				pass
			if variable.FieldType == "DecimalField":
				modeldetails = "%s, max_digits=%s, decimal_places=%s" % (modeldetails, variable.VarMaxDigits, variable.VarMaxDecimalPlaces)
			elif variable.FieldType == "CharField":
				modeldetails = "%s, max_length=%s" % (modeldetails, variable.VarMaxLength)
			else:
				pass
			if variable.FieldType.strip() == "RadioButton":
				FieldType = "BigIntegerField"
			else:
				FieldType = variable.FieldType.strip()
			VariableWrite.append("%s = models.%s(%s)" % (variable.VarName.strip(), FieldType, modeldetails))
		modelWriter.write(
"""\n\nclass %s(models.Model):
	%s
		""" % (form.FormName, "\n\t".join(VariableWrite)))


def writeForms(Project):
	newForms = open("../newdanger/stroke/doubt/forms.py", "w+")
	formWriter = open("../newdanger/stroke/doubt/forms.py", "a")
	formWriter.write(
"""from %s.models import *
from %s.options import *
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, RadioSelect
from django.forms.util import ErrorList
import re\n\n""" % (Project[0].ProjectID.ProjectURL, Project[0].ProjectID.ProjectURL))
	for form in Project:
		formWriter.write("""
class mf%s(ModelForm):
	class Meta:
		model = %s
		widgets = {""" % (form.FormName.strip(), form.FormName.strip()))
		for variable in form.Variable.all():
			if variable.FieldType == "RadioButton":
				formWriter.write("\n\t\t'%s': RadioSelect(choices=%s_%s)," % (variable.VarName.strip(), form.FormName.strip(), variable.VarName.strip()))
		formWriter.write("""}
	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(mf%s, self).__init__(*args, **kwargs)\n\n""" % form.FormName.strip())


def writeOptions(Project):
	newOptions = open("../newdanger/stroke/doubt/options.py", "w+")
	optionWriter = open("../newdanger/stroke/doubt/options.py", "a")
	for form in Project:
		for variable in form.Variable.all():
			if variable.FieldType == "RadioButton":
				Choices = []
				for option in variable.Option.all():
					values = ()
					newLab = re.sub("'", "\\'", str(option.Label.strip()))
					newVal = int(option.Value)
					values = values + (newVal, newLab)
					Choices.append(values)
				optionWriter.write("%s_%s = %r \n\n" % (form.FormName.strip(), variable.VarName.strip(), Choices))
			else:
				pass

def writeAdmins(Project):
	newAdmins = open("../newdanger/stroke/doubt/admin.py", "w+")
	adminWriter = open("../newdanger/stroke/doubt/admin.py", "a")
	adminWriter.write(
"""from django.contrib import admin
from %s.models import *
import reversion

class VersioningAdmin(reversion.VersionAdmin):
    pass\n\n""" % (Project[0].ProjectID.ProjectURL))
	for form in Project:
		adminWriter.write("admin.site.register(%s, VersioningAdmin)\n\n" % form.FormName.strip())







