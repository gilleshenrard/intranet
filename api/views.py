from rest_framework.decorators import api_view
from django.http.response import HttpResponseNotFound
import logging

stdlogger = logging.getLogger(__name__)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_profile(request, usrname):

    # get details of a single profile
    if request.method == 'GET':
        stdlogger.info("API_get : request for single profile retrieval")
        return HttpResponseNotFound()

    # delete a single profile
    elif request.method == 'DELETE':
        stdlogger.info("API_delete : request for single profile deletion")
        return HttpResponseNotFound()

    # update details of a single profile
    elif request.method == 'PUT':
        stdlogger.info("API_put : request for single profile update")
        return HttpResponseNotFound()


@api_view(['GET', 'POST'])
def get_post_profiles(request):
    # get all profiles
    if request.method == 'GET':
        stdlogger.info("API_get_all : request for all profiles retrieval")
        return HttpResponseNotFound()

    # insert a new record for a profile
    elif request.method == 'POST':
        stdlogger.info("API_post : request for single profile creation")
        return HttpResponseNotFound()
