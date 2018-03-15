from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from requests import get
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import logging

stdlogger = logging.getLogger(__name__)


def home(request):
    """Handles home page behaviour and rendering"""
    stdlogger.info("HOME : request for home page")

    if request.method == "POST":
        # login form sent
        stdlogger.info("HOME_post : login request received")
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            # login data is valid
            stdlogger.debug("HOME_post : login form data is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                stdlogger.info("HOME_post : user '" + username + "' successfully authenticated")
                messages.add_message(request, messages.SUCCESS, 'You are now authenticated')

        else:
            # login data is invalid
            stdlogger.error("HOME_post : login form data is invalid")
            for field, errors in form.errors.items():
                for error in errors:
                    stdlogger.error(field + " -> " + error)
                    messages.add_message(request, messages.ERROR, field + " : " + error)

    r = get("http://localhost:8000" + reverse("get_post_profiles"))
    if r.status_code == status.HTTP_200_OK:
        stdlogger.info("HOME_get : All profiles successfully retrieved.")
        return render(request, 'web/home.html', {'users': r.json()})
    else:
        stdlogger.error("HOME_get : Profiles could not be found.")
        return HttpResponseNotFound("Profiles not found.")


def user_logout(request):
    """Handles user logout and redirects to home page"""
    stdlogger.info("LOGOUT : logout request received")
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You are now logged out')
    return redirect(reverse('home'))


def profile(request, usrname):
    """Handles profile page behaviour and rendering"""

    stdlogger.info("PROFILE : request for profile of '" + usrname + "'")
    return HttpResponseNotFound()
