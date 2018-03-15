from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from requests import get
from rest_framework import status
from django.core.urlresolvers import reverse
import logging

stdlogger = logging.getLogger(__name__)


def home(request):
    """Handles home page behaviour and rendering"""
    stdlogger.info("HOME : request for home page")

    r = get("http://localhost:8000" + reverse("get_post_profiles"))
    if r.status_code == status.HTTP_200_OK:
        stdlogger.info("HOME : All profiles successfully retrieved.")
        return render(request, 'web/home.html', {'users': r.json()})
    else:
        stdlogger.error("HOME : Profiles could not be found.")
        return HttpResponseNotFound("Profiles not found.")


def profile(request, usrname):
    """Handles profile page behaviour and rendering"""

    stdlogger.info("PROFILE : request for profile of '" + usrname + "'")
    return HttpResponseNotFound()
