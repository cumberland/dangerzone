from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from newage.models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.shortcuts import get_object_or_404

import datetime
from datetime import timedelta
from datetime import datetime

def newage(request):
	Names = Name.objects.all()
	if request.method == "POST":
		saveForm = mfName(request.POST)
		if saveForm.is_valid():
			saveForm.save()
			return HttpResponseRedirect("/newage/")
		else:
			return render_to_response('newage.html', {'Names': Names, 'newForm': saveForm}, RequestContext(request))
	else:
		newForm = mfName()
		return render_to_response('newage.html', {'Names': Names, 'newForm': newForm}, RequestContext(request))


def newageedit(request, test_id):
	Names = Name.objects.all()
	if request.method == "POST":
		newForm = mfName(request.POST, instance=Name.objects.get(id=test_id))
		if newForm.is_valid():
			newForm.save()
			return HttpResponseRedirect("/newageedit/")
		else:
			pass
	else:
		newForm = mfName(instance=Name.objects.get(id=test_id))
	return render_to_response('newage.html', {'Names': Names, 'newForm': newForm}, RequestContext(request))

def newageset(request):
	# Names = NewName.objects.all()
	if request.method == "POST":
		newForm = SeizureFormSet(request.POST)
		if newForm.is_valid():
			newForm.save()
			return HttpResponseRedirect("/newageset/")
		else:
			return render_to_response('newage.html', {'Names': Names, 'newForm': newForm}, RequestContext(request))
	else:
		newForm = SeizureFormSet()
		return render_to_response('dynamicexample.html', {'newForm': newForm}, RequestContext(request))


from django.views.generic import View, TemplateView

class MyView(View):
	
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello, World!")



class HomePageView(TemplateView):

	template_name="home.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['latest_names'] = NewName.objects.all()
		return context


