from django.http.response import HttpResponseNotFound
import logging

stdlogger = logging.getLogger(__name__)


def home(request):
    """Handles home page behaviour and rendering"""

    stdlogger.info("HOME : request for home page")
    return HttpResponseNotFound()


def profile(request, usrname):
    """Handles profile page behaviour and rendering"""

    stdlogger.info("profile : request for profile of '" + usrname + "'")
    return HttpResponseNotFound()
