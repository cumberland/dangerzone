import re
CogReg = []

with open("cogregrevamp.txt", "r") as f:
	models = f.read()
	models = models.split("\n\n")
	for i in models:
		if i:
			i = ''.join(i.split())
			CogReg.append(i)


CNC = []

for i in CogReg:
	print i
	VarDef = {}
	VarDef['VarName'] = re.findall(r'classmo([^(]+)', i)
	VarDef['FieldType'] = re.findall(r'=models\.([^(]+)', i)
	CNC.append(VarDef)
	
for i in CNC:
	if len(i['VarName']) != 1 or i['VarName'] == "":
		print i
	print i['FieldType']