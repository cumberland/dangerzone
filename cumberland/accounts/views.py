from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

def index(request):
	renderDict = {}
	return render_to_response('index.html', renderDict, RequestContext(request))

def indexroundabout(request):
	renderDict = {}
	return render_to_response('index-roundabout.html', renderDict, RequestContext(request))

from accounts.models import InviteForm
from django.views.generic.edit import FormView

# def invite(request):
# 	renderDict = {}
# 	return render_to_response('invite.html', renderDict, RequestContext(request))

class InviteView(FormView):
    template_name = 'invite.html'
    form_class = InviteForm
    success_url = reverse_lazy('accounts.views.indexroundabout')

    def get_context_data(self, **kwargs):
    	kwargs['user_list'] = User.objects.all()
    	return super(InviteView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(InviteView, self).form_valid(form)

