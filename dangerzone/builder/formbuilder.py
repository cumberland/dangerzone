
	VarList = VariableDescription.objects.all()
	printList = []
	for variable in VarList:
		if variable.FieldType == "BooleanField":
			pass
		else:
			modeldetails = "blank=%s, null=%s" % (variable.VarBlank, variable.VarNull)
		if variable.FieldType == "DecimalField":
			modeldetails = "%s, "
		elif variable.FieldType == "BooleanField":
			pass
		elif variable.FieldType == "CharField":
			pass
		elif variable.FieldType == "TextField":
			pass
		elif variable.FieldType == "DateField":
			pass
		elif variable.FieldType == "TimeField":
			pass
		elif variable.FieldType == "DateTimeField":
			pass
		else:
			print "Something went wrong."
		printList.append("""
class mo%s(Audit):
	mv%s = models.%s(verbose_name=%s)
	def __unicode__(self):
		return "%%s" %% self.mv%s
	class Meta:
		get_latest_by = 'record'
		""" % (variable.VarName, variable.VarName, variable.FieldType, variable.VarLabel, variable.VarName))


class moHUILocation(Audit):
	mvHUILocation = models.BigIntegerField(verbose_name="Where was HUI completed?", blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvHUILocation
	class Meta:
		get_latest_by = 'record'





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
	

# options = []

# values = ()
# values = values + (1,"Something")
# options.append(values)
# newChoices = """co%s = %r \n\n""" % ("Test", options)
# print newChoices


