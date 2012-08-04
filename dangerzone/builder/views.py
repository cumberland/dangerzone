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



def login_main_page(request):
    return render_to_response('base.html', RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def xhr_test(request):
	if request.is_ajax():
		if request.method == "POST":
			test = [{'absolute_url': 'blah', 'url_name': 'blah', 'message': 'blah', 'type': 'blah'}, {'absolute_url': 'foo', 'url_name': 'foo', 'message': 'foo', 'type': 'foo'}]
			json = simplejson.dumps(test)
		else:
			message = "Hello Giddy Baby"
		return HttpResponse(json, mimetype="text/json")
	else:
		pass


@login_required(login_url='/login/')
def project(request):
	renderDict = {}
	if request.method == "POST":
		newForm = mfVariableDescription(request, request.POST)
		if newForm.is_valid():
			getProject = ProjectName.objects.get(id=request.session['ProjectID'])
			instance = newForm.save(commit=False)
			instance.ProjectID = getProject
			instance.user = request.user.username
			instance.save()
			return HttpResponseRedirect("/project/")
		else:
			renderDict['newForm'] = newForm
	else:
		try:
			ProjectID = request.session['ProjectID']
		except:
			return HttpResponseRedirect('/main/')
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
			renderDict['newForm'] = mfProjectName(instance=ProjectName.objects.filter(id=request.session['ProjectID']).latest())
		except:
			renderDict['newForm'] = mfProjectName()
	renderDict['ProjectList'] = ProjectName.objects.all()
	return render_to_response('main.html', renderDict, RequestContext(request))


@login_required(login_url='/login/')
def activeproject(request):
	try:
		request.session['ProjectID'] = int(request.POST['ProjectID'])
	except:
		try:
			del request.session['ProjectID']
		except:
			pass
	try:
		del request.session['VarID']
	except:
		pass
	return HttpResponseRedirect('/main/')


@login_required(login_url='/login/')
def activevar(request):
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







