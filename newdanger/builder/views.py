from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from builder.models import *
from builder.forms import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from builder.formbuilder import writeModels, writeForms, writeOptions, writeAdmins
from builder.templatebuilder import writeTemplates
from django.core.urlresolvers import reverse


def xhr_test(request):
	if request.is_ajax():
		if request.method == "POST":
			errors = []
			try:
				OptionValue = int(request.POST['OptionValue'])
			except:
				errors.append("int() didn't work")
			OptionLabel = request.POST['OptionLabel']
			try:
				getProject = ProjectName.objects.filter(id=request.session['ProjectID']).latest()
			except:
				errors.append("project didn't work")
			try:
				getVar = VariableDescription.objects.filter(ProjectID=request.session['ProjectID'], id=request.session['VarID']).latest()
			except:
				errors.append("var didn't work")
			newOption = Options(ProjectID=getProject,
								VarID=getVar,
								Value=OptionValue,
								Label=OptionLabel,
								user=request.user)
			try:
				newOption.save()
			except:
				errors.append("save didn't work")
			# test = [{'absolute_url': 'blah', 'url_name': 'blah', 'message': 'blah', 'type': 'blah'}, {'absolute_url': 'foo', 'url_name': 'foo', 'message': 'foo', 'type': 'foo'}]
			json = simplejson.dumps(errors)
		else:
			message = "Hello Giddy Baby"
		return HttpResponse(json, mimetype="text/json")
	else:
		pass



@login_required(login_url='/login/')
def project(request):
	renderDict = {}
	try:
		ProjectID = request.session['ProjectID']
	except:
		return HttpResponseRedirect('/main/')
	if request.method == "POST":
		newForm = mfVariableDescription(request, request.POST)
		if newForm.is_valid():
			getProject = ProjectName.objects.get(id=request.session['ProjectID'])
			instance = newForm.save(commit=False)
			instance.ProjectID = getProject
			instance.user = request.user.username
			Type = instance.FieldType
			instance.save()
			return HttpResponseRedirect("/project/")	
		else:
			renderDict['newForm'] = newForm
	else:
		try:
			renderDict['newForm'] = mfVariableDescription(request, instance=VariableDescription.objects.filter(ProjectID=ProjectID, id=request.session['VarID']).latest())
		except:
			renderDict['newForm'] = mfVariableDescription(request)
	renderDict['VarList'] = VariableDescription.objects.filter(ProjectID=ProjectID)
	return render_to_response('project.html', renderDict, RequestContext(request))

			






@login_required(login_url='/login/')
def activevar(request):
	if request.is_ajax():
		errors = []
		try:
			VarID = request.POST['VarID']
		except:
			errors.append("VarID no work.")
		try:
			Var = VariableDescription.objects.filter(id=VarID).latest()
		except:
			errors.append("Retrieve VarID no work.")
		try:
			response = {'VarName': Var.VarName, 'VarLabel': Var.VarLabel, 'VarDescription': Var.VarDescription, 'user': Var.user, 'FieldType': Var.FieldType}
		except:
			errors.append("Dict no work.")
		json = simplejson.dumps(response)
		return HttpResponse(json, mimetype="text/json")
	else:
		try:
			request.session['VarID'] = int(request.POST['VarID'])
		except:
			try:
				del request.session['VarID']
			except:
				pass
		return HttpResponseRedirect('/project/')


@login_required(login_url='/login/')
def varsummary(request):
	# try:
	# 	ProjectID = request.session['ProjectID']
	# 	VarID = request.session['VarID']
	# except:
	# 	return HttpResponseRedirect("/main/")
	return render_to_response('varsummary.html', RequestContext(request))






def testprint(request):
	models = modelWrite(VariableDescription.objects.filter(ProjectID=2), "cncr")
	forms = formWrite(VariableDescription.objects.filter(ProjectID=2), "cncr")
	options = optionWrite(VariableDescription.objects.filter(ProjectID=2, FieldType="RadioButton"), "cncr")
	admin = adminWrite(VariableDescription.objects.filter(ProjectID=2), "cncr")
	return render_to_response('testprint.html', RequestContext(request))

######################################################################
#################--START: Properly Converted Views--##################
######################################################################

def login_main_page(request):
    return render_to_response('base.html', RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))


def main(request):
	if request.user.is_authenticated():
		try:
			del request.session['ProjectID']
		except KeyError:
			pass
		try:
			del request.session['FormID']
		except KeyError:
			pass
		try:
			del request.session['VarID']
		except KeyError:
			pass		
		renderDict = {}
		if request.method == "POST":
			newForm = mfProject(request.POST)
			if newForm.is_valid():
				newForm.save()	
				return HttpResponseRedirect(reverse('builder.views.main'))
			else:
				renderDict['newForm'] = newForm
		else:
			try:
				del request.session['ProjectID']
			except:
				pass
			renderDict['newForm'] = mfProject()
		renderDict['ProjectList'] = Project.objects.all()
		return render_to_response('main.html', renderDict, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def form(request):
	"""
	Creating new forms for a :model:`builder.ProjectName`

	**POST**

	Check if new :model:`builder.Forms` is valid. If valid save and reload and if not valid load with errors.

	**GET**

	Load blank ModelForm for :model:`builder.Forms`.

	**TEMPLATE**

	:template:`form.html`

	"""
	if request.user.is_authenticated():
		try:
			del request.session['FormID']
		except KeyError:
			pass		
		try:
			del request.session['VarID']
		except KeyError:
			pass		
		renderDict = {}
		try:
			ProjectID = request.session['ProjectID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.main'))
		if request.method == "POST":
			newForm = mfForm(request, request.POST)
			if newForm.is_valid():
				instance = newForm.save(commit=False)
				instance.save()
				FormCopy = request.POST['FormCopy']
				if FormCopy != "Create New":
					newCopyForm = Form.objects.get(ProjectID=ProjectID, FormName=FormCopy)
					newVariableOrder = []
					for Var in newCopyForm.Variable.all():
						Var.id = None
						Var.FormID = instance
						Var.save()
						newVariableOrder.append(Var.id)
					instance.VariableOrder = newVariableOrder
					instance.save()
				else:
					pass	
				return HttpResponseRedirect(reverse('builder.views.form'))
			else:
				renderDict['newForm'] = newForm
		else:
			renderDict['newForm'] = mfForm(request)
		renderDict['FormList'] = Form.objects.filter(ProjectID=ProjectID)
		return render_to_response('form.html', renderDict, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def activeproject(request):
	"""
	Setting the active :model:`builder.ProjectName`

	**AJAX**

	When in :view:`builder.views.main` an ajax request sets the current :model:`builder.ProjectName` being viewed.

	**POST**

	When directing to :view:`builder.views.form` sets the session variable of ProjectID to the instance of :model:`builder.ProjectName`
	that is having its forms altered.

	"""
	if request.user.is_authenticated():
		if request.is_ajax():
			ProjectID = request.POST['ProjectID']
			activeProject = Project.objects.get(id=ProjectID)
			response = {'ProjectName': activeProject.ProjectName, 'ProjectDescription': activeProject.ProjectDescription}
			json = simplejson.dumps(response)
			return HttpResponse(json, mimetype="text/json")
		else:
			try:
				request.session['ProjectID'] = Project.objects.get(id=int(request.POST['ProjectID']))
			except:
				return HttpResponseRedirect(reverse('builder.views.main'))
			else:
				return HttpResponseRedirect(reverse('builder.views.form'))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def activeform(request):
	if request.user.is_authenticated():
		try:
			del request.session['VarID']
		except KeyError:
			pass		
		if request.method == "POST":
			activeForm = request.POST['FormID']
			try:
				activeForm = int(activeForm)
			except:
				try:
					del request.session['FormID']
				except:
					pass
				return HttpResponseRedirect(reverse('builder.views.form'))
			try:
				request.session['FormID'] = Form.objects.get(id=activeForm)
			except:
				pass
			return HttpResponseRedirect(reverse('builder.views.variable'))
		else:
			try:
				del request.session['FormID']
			except:
				pass
			return HttpResponseRedirect(reverse('builder.views.form'))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

def variable(request):
	if request.user.is_authenticated():
		renderDict = {}
		try:
			ProjectID = request.session['ProjectID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.main'))
		try:
			FormID = request.session['FormID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.form'))
		if request.method == "POST":
			try:
				newForm = mfVariable(request, request.POST, instance=request.session['VarID'])
			except:
				newForm = mfVariable(request, request.POST)
			if newForm.is_valid():
				instance = newForm.save(commit=False)
				testID = instance.id
				instance.save()
				if not testID:
					updateOrder = request.session['FormID']
					changeOrder = eval(updateOrder.VariableOrder)
					changeOrder.append(instance.id)
					updateOrder.VariableOrder = changeOrder
					updateOrder.save()
					request.session['FormID'] = Form.objects.get(id=updateOrder.id)
				return HttpResponseRedirect(reverse('builder.views.variable'))
			else:
				renderDict['newForm'] = newForm
		elif 'VarID' in request.GET:
			VarID = request.GET['VarID']
			try:
				VarID = int(VarID)
			except ValueError:
				try:
					del request.session['VarID']
				except:
					pass
				return HttpResponseRedirect(reverse('builder.views.variable'))
			else:
				request.session['VarID'] = Variable.objects.get(id=VarID)
				renderDict['newForm'] = mfVariable(request, instance=request.session['VarID'])
		else:
			try:
				del request.session['VarID']
			except KeyError:
				pass
			renderDict['newForm'] = mfVariable(request)
		VarList = []
		for OrderID in eval(request.session['FormID'].VariableOrder):
			VarList.append(Variable.objects.get(id=OrderID))
		renderDict['VarList'] = VarList
		renderDict['FormList'] = Form.objects.filter(ProjectID=ProjectID)
		return render_to_response('variable.html', renderDict, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))


def bulkvariable(request):
	if request.user.is_authenticated():
		renderDict = {}
		try:
			ProjectID = request.session['ProjectID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.main'))
		try:
			FormID = request.session['FormID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.form'))
		if request.method == "POST":
			try:
				newForm = mfVariable(request, request.POST, instance=request.session['VarID'])
			except:
				newForm = mfVariable(request, request.POST)
			if newForm.is_valid():
				instance = newForm.save(commit=False)
				testID = instance.id
				instance.save()
				if not testID:
					updateOrder = request.session['FormID']
					changeOrder = eval(updateOrder.VariableOrder)
					changeOrder.append(instance.id)
					updateOrder.VariableOrder = changeOrder
					updateOrder.save()
					request.session['FormID'] = Form.objects.get(id=updateOrder.id)
				return HttpResponseRedirect(reverse('builder.views.variable'))
			else:
				renderDict['newForm'] = newForm
		elif 'VarID' in request.GET:
			VarID = request.GET['VarID']
			try:
				VarID = int(VarID)
			except ValueError:
				try:
					del request.session['VarID']
				except:
					pass
				return HttpResponseRedirect(reverse('builder.views.variable'))
			else:
				request.session['VarID'] = Variable.objects.get(id=VarID)
				renderDict['newForm'] = mfVariable(request, instance=request.session['VarID'])
		else:
			try:
				del request.session['VarID']
			except KeyError:
				pass
			VariableFormSet = modelformset_factory(Variable, form=mfVariable, extra=3, formset=BaseAuthorFormSet)
			renderDict['newForm'] = VariableFormSet(queryset=Variable.objects.filter(FormID=request.session['FormID']))
		VarList = []
		for OrderID in eval(request.session['FormID'].VariableOrder):
			VarList.append(Variable.objects.get(id=OrderID))
		renderDict['VarList'] = VarList
		renderDict['FormList'] = Form.objects.filter(ProjectID=ProjectID)
		return render_to_response('bulkvariable.html', renderDict, RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))



def currentoptions(request):
	if request.is_ajax():
		currentOptions = Option.objects.filter(VariableID=int(request.POST['VarID']))
		response = []
		for i in currentOptions:
			vallabel = {}
			vallabel['OptionID'] = i.id
			vallabel['OptionValue'] = i.Value
			vallabel['OptionLabel'] = i.Label
			response.append(vallabel)
		json = simplejson.dumps(response)
		return HttpResponse(json, mimetype="text/json")
	else:
		pass

def addoption(request):
	if request.is_ajax():
		errors = []
		try:
			OptionValue = int(request.POST['OptionValue'])
		except:
			errors.append("int() didn't work")
		OptionLabel = request.POST['OptionLabel']
		try:
			VariableID = int(request.POST['VariableID'])
		except:
			errors.append("project didn't work")
		try:
			getVar = Variable.objects.get(id=VariableID)
		except:
			errors.append("var didn't work")
		newOption = Option(VariableID=getVar,
							Value=OptionValue,
							Label=OptionLabel)
		try:
			newOption.save()
		except:
			errors.append("save didn't work")
		response = {'OptionValue': OptionValue, 'OptionLabel': OptionLabel, 'OptionID': newOption.id}
		json = simplejson.dumps(response)
		return HttpResponse(json, mimetype="text/json")
	else:
		pass

def deleteoption(request):
	if request.is_ajax():
		Option.objects.filter(id=int(request.POST['OptionID'])).delete()
		return HttpResponse("Deleted.")
	else:
		pass

def deletevariable(request):
	if request.is_ajax():
		VariableID = int(request.POST['VariableID'])
		Variable.objects.filter(id=VariableID).delete()
		updateOrder = request.session['FormID']
		changeOrder = eval(updateOrder.VariableOrder)
		changeOrder.remove(VariableID)
		updateOrder.VariableOrder = changeOrder
		updateOrder.save()
		request.session['FormID'] = Form.objects.get(id=updateOrder.id)
		return HttpResponse(request.POST['VariableID'])
	else:
		pass

def variableorder(request):
	if request.is_ajax():
		Order = request.POST['Order']
		newOrder = []
		for i in eval(Order):
			 newOrder.append(int(i.strip("liid_")))
		updateOrder = request.session['FormID']
		updateOrder.VariableOrder = newOrder
		updateOrder.save()
		request.session['FormID'] = Form.objects.get(id=updateOrder.id)
		return HttpResponse(request.POST['Order'])
	else:
		pass

def projectprinter(request):
	renderDict = {}
	ProjectID = int(request.POST['ProjectID'])
	writeModels(Form.objects.filter(ProjectID=ProjectID))
	writeOptions(Form.objects.filter(ProjectID=ProjectID))
	writeForms(Form.objects.filter(ProjectID=ProjectID))
	writeAdmins(Form.objects.filter(ProjectID=ProjectID))
	return render_to_response('printout.html', renderDict, RequestContext(request))

def templateprinter(request):
	renderDict = {}
	# ProjectID = int(request.POST['ProjectID'])
	writeTemplates(Form.objects.get(FormName="CT"))
	# writeOptions(Form.objects.filter(ProjectID=ProjectID))
	# writeForms(Form.objects.filter(ProjectID=ProjectID))
	# writeAdmins(Form.objects.filter(ProjectID=ProjectID))
	return render_to_response('printout.html', renderDict, RequestContext(request))

def copyvar(request):
	if request.user.is_authenticated():
		renderDict = {}
		try:
			ProjectID = request.session['ProjectID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.main'))
		try:
			FormID = request.session['FormID']
		except KeyError:
			return HttpResponseRedirect(reverse('builder.views.form'))
		if request.method == "POST":
			try:
				VarID = int(request.POST['VarID'])
			except:
				pass
			copyVar = Variable.objects.get(id=VarID)
			copyOptions = Option.objects.filter(VariableID=copyVar)
			copyVar.id = None
			copyVar.VarName = copyVar.VarName+"_1"
			copyVar.save()
			for opt in copyOptions:
				opt.id = None
				opt.VariableID = copyVar
				opt.save()
			updateOrder = request.session['FormID']
			changeOrder = eval(updateOrder.VariableOrder)
			changeOrder.append(copyVar.id)
			updateOrder.VariableOrder = changeOrder
			updateOrder.save()
			request.session['FormID'] = Form.objects.get(id=updateOrder.id)
		else:
			pass
		return HttpResponseRedirect(reverse('builder.views.variable'))
	else:
		return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))


######################################################################
##################--END: Properly Converted Views--###################
######################################################################
