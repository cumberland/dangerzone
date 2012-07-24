from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from simpleform.models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User

def login_main_page(request):
    return render_to_response('base.html', RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def xhr_test(request):
    if request.is_ajax():
        message = "Hello Giddy Baby"
    else:
        message = "Hello"
    return HttpResponse(message)

def project(request):
	if request.method == "POST":
		try:
			ProjectID = int(request.POST['ProjectID'])
			request.session['ProjectID'] = ProjectID
			return HttpResponseRedirect('/start/')
		except:
			return HttpResponseRedirect('/main/')
	else:
		return HttpResponseRedirect('/main/')


def start(request):
	if request.method == "POST":
		try:
			ProjectID = request.session['ProjectID']
			VarList = VariableDescription.objects.filter(ProjectID=ProjectID)
		except:
			return HttpResponseRedirect('/main/')
		try:
			VarID = request.POST['VarID']
		except:
			VarID = []
		if VarID == "New":
			newForm = mfVariableDescription()
		elif not VarID:
			newForm = mfVariableDescription(request.POST)
			getProject = ProjectName.objects.get(id=request.session['ProjectID'])
			if newForm.is_valid():
				instance = newForm.save(commit=False)
				instance.ProjectID = getProject
				instance.save()
				return HttpResponseRedirect("/start/")
		else:
			newForm = mfVariableDescription(instance=VariableDescription.objects.filter(ProjectID=request.session['ProjectID'], VarName=VarID))
		return render_to_response('start.html', {'newForm': newForm, 'VarList': VarList}, RequestContext(request))
	else:
		try:
			ProjectID = request.session['ProjectID']
			VarList = VariableDescription.objects.filter(ProjectID=ProjectID)
		except:
			return HttpResponseRedirect('/main/')
		newForm = mfVariableDescription()
		return render_to_response('start.html', {'newForm': newForm, 'VarList': VarList}, RequestContext(request))
			

def main(request):
	if request.method == "POST":
		newForm = mfProjectName(request.POST)
		if newForm.is_valid():
			newForm.save()
			return HttpResponseRedirect("/main/")
		else:
			ProjectList = ProjectName.objects.all()
			return render_to_response('main.html', {'newForm': newForm, 'ProjectList': ProjectList}, RequestContext(request))
	else:
		try:
			del request.session['ProjectID']
		except:
			pass
		newForm = mfProjectName()
		ProjectList = ProjectName.objects.all()
		return render_to_response('main.html', {'newForm': newForm, 'ProjectList': ProjectList}, RequestContext(request))




