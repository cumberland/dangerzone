from builder.models import Option
import re

# Outine Process
# Startapp - 1) Create folder with slug name 2) __init__.py the folder 3) Create the files that will be used
# i) admin.py
# ii) forms.py
# iii) models.py - DONE
# iv) urls.py
# v) choices.py
# vi) views.py

def writeModels(Project):
	newModels = open("../newdanger/testprint/models.py", "w+")
	modelWriter = open("../newdanger/testprint/models.py", "a")
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


def formWrite(VarList, location):
	formWriter = open("../dangerzone/"+location+"/forms.py", "w+")
	# printList = []
	for variable in VarList:
		if variable.FieldType == "RadioButton":
			widget = """
widgets = {
	'mv%s': RadioSelect(choices=co%s)
	}
""" % (variable.VarName.strip(), variable.VarName.strip())
		else:
			widget=""
		formWriter.write("""
class mf%s(ModelForm):
	class Meta:
		model = mo%s
		%s
		\n\n""" % (variable.VarName.strip(), variable.VarName.strip(), widget))
	# return printList

def optionWrite(VarList, location):
	optionWriter = open("../dangerzone/"+location+"/options.py", "w+")
	# printList = []
	for variable in VarList:
		OptionList = Options.objects.filter(VarID=variable)
		Choices = []
		for option in OptionList:
			values = ()
			newLab = re.sub("'", "\\'", str(option.Label.strip()))
			newVal = int(option.Value)
			values = values + (newVal, newLab)
			Choices.append(values)
		optionWriter.write("co%s = %r \n\n" % (variable.VarName.strip(), Choices))
	# return printList

def adminWrite(VarList, location):
	adminWriter = open("../dangerzone/"+location+"/admin.py", "w+")
	# printList = []
	for variable in VarList:
		adminWriter.write("admin.site.register(mo%s)\n\n" % variable.VarName.strip())
	for variable in VarList:
		adminWriter.write("%s*" % variable.VarName.strip())
	# return printList



# class moHUILocation(Audit):
# 	mvHUILocation = models.BigIntegerField(verbose_name="Where was HUI completed?", blank=False, null=False)
# 	def __unicode__(self):
# 		return "%s" % self.mvHUILocation
# 	class Meta:
# 		get_latest_by = 'record'





# 	ProjectID = models.ForeignKey(ProjectName, default=0, editable=False)
# 	VarLabel = models.CharField(max_length=500, verbose_name="Label of variable on form:") # verbose_name
# 	VarName = models.CharField(max_length=62, verbose_name="Name of variable in the database:") # variable name
# 	VarDescription = models.CharField(max_length=500, verbose_name="Description of what the variable is collecting:") # description of variable purpose
# 	FieldType = models.CharField(max_length=20, choices=FieldChoices, verbose_name="Variable type:") # variable type
# 	VarBlank = models.BooleanField(verbose_name="Blank values are allowed.")
# 	VarNull = models.BooleanField(verbose_name="Null values are allowed.")
# 	Identifier = models.BooleanField(verbose_name="Collects identifiable information.")
# 	VarMaxDigits = models.PositiveIntegerField(verbose_name="Maximum number of digits allowed (required):", blank=True, null=True)
# 	VarMaxDecimalPlaces = models.PositiveIntegerField(verbose_name="Maximum number of decimal places allowed (required):", blank=True, null=True)
# 	VarMaxLength = models.PositiveIntegerField(verbose_name="Maximum number of characters allowed (required):", blank=True, null=True)
	






