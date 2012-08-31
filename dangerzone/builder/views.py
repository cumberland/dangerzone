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
from builder.formbuilder import modelWrite, formWrite, optionWrite, adminWrite


def login_main_page(request):
    return render_to_response('base.html', RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

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
def main(request):
	renderDict = {}
	if request.method == "POST":
		newForm = mfProjectName(request.POST)
		if newForm.is_valid():
			newForm.save()	
			return HttpResponseRedirect("/main/")
		else:
			renderDict['newForm'] = newForm
	else:
		try:
			del request.session['VarID']
		except:
			pass
		try:
			del request.session['ProjectID']
		except:
			pass
		renderDict['newForm'] = mfProjectName()
	renderDict['ProjectList'] = ProjectName.objects.all()
	return render_to_response('main.html', renderDict, RequestContext(request))


@login_required(login_url='/login/')
def activeproject(request):
	if request.is_ajax():
		ProjectID = request.POST['ProjectID']
		Project = ProjectName.objects.filter(id=ProjectID).latest()
		response = {'Project': Project.Project, 'ProjectDescription': Project.ProjectDescription}
		json = simplejson.dumps(response)
		return HttpResponse(json, mimetype="text/json")
	else:
		try:
			request.session['ProjectID'] = int(request.POST['ProjectID'])
		except:
			return HttpResponseRedirect('/main/')
		try:
			del request.session['VarID']
		except:
			pass
		return HttpResponseRedirect('/project/')


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

def addoption(request):
	if request.is_ajax():
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
			getVar = VariableDescription.objects.filter(id=int(request.POST['VarID'])).latest()
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
		response = {'OptionValue': OptionValue, 'OptionLabel': OptionLabel, 'OptionID': newOption.id}
		json = simplejson.dumps(response)
		return HttpResponse(json, mimetype="text/json")
	else:
		pass



def currentoptions(request):
	if request.is_ajax():
		currentOptions = Options.objects.filter(VarID=int(request.POST['VarID']))
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

def deleteoption(request):
	if request.is_ajax():
		Options.objects.filter(id=int(request.POST['OptionID'])).delete()
		return HttpResponse("Deleted.")
	else:
		pass


def testprint(request):
	models = modelWrite(VariableDescription.objects.all(), "needs")
	forms = formWrite(VariableDescription.objects.all(), "needs")
	options = optionWrite(VariableDescription.objects.filter(FieldType="RadioButton"), "needs")
	admin = adminWrite(VariableDescription.objects.all(), "needs")
	return render_to_response('testprint.html', RequestContext(request))


@login_required(login_url='/login/')
def form(request):
	renderDict = {}
	if request.method == "POST":
		renderDict['dictionary'] = request.POST['Variable']
		return render_to_response('form.html', renderDict, RequestContext(request))
		# if newForm.is_valid():
		# 	newForm.save()	
		# 	return HttpResponseRedirect("/main/")
		# else:
		# 	renderDict['newForm'] = newForm
	else:
		try:
			del request.session['VarID']
		except:
			pass
		try:
			del request.session['ProjectID']
		except:
			pass
		renderDict['newForm'] = mfForms()
	return render_to_response('form.html', renderDict, RequestContext(request))

