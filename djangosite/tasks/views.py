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

def register(request):
    context = RequestContext(request)
    # boolean to determine if registation was succesful
    registered = False
    # if HTTP post then process from data
    if request.method == 'POST':
        # grab info
        user_form = UserForm(data = request.POST)
        #profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid():
            # save form to dadabase
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # sort user profile instance, set as false to avoid integrity problems
            #profile = profile_form.save(commit = False)
            #proifle.user = user
            registered = True
        else:
            # if form not complete or wrong
            print(user_form.errors)
    else:
        user_form = UserForm()
        #profile form doesn't work, cant get django to add ID#
        #profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'registered': registered}
    return render_to_response('tasks/index.html', context_dict, context)


def user_login(request):
    # Obtain our request's context.
    context = RequestContext(request)
    context_dict = {}

    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to log the user in with the supplied credentials.
        # A User object is returned if correct - None if not.
        user = authenticate(username=username, password=password)

        # A valid user logged in?
        if user is not None:
            # Check if the account is active (can be used).
            # If so, log the user in and redirect them to the homepage.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tasks/')
            # The account is inactive tell by adding variable to the template context.
            else:
                context_dict['disabled_account'] = True
                return render_to_response('tasks/index.html', context_dict, context)
        # Invalid login details supplied
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            context_dict['bad_details'] = True
            return render_to_response('tasks/index.html', context_dict, context)

    # Not a HTTP POST - most likely a HTTP GET. In this case, we render the login form for the user.
    else:
        return render_to_response('tasks/index.html', context_dict, context)

