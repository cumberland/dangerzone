
	Project = request.session['project']
	VarList = VariableDescription.objects.filter(Project=Project)
	for Var in VarList:
		verbose_name = Var.VarLabel
		varname = Var.VarName
		fieldtype = Var.FieldType
		blank = Var.VarBlank
		null = Var.VarNull
		
	