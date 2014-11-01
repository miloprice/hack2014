from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

def index(request):
    context = RequestContext(request)
    context_dict = {}
#    if request.user.is_authenticated():
#        user = str(request.user.get_full_name())
#        context_dict['str_user']=user
    return render_to_response('tasks/index.html', context_dict, context)
