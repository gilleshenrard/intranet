from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
import logging

stdlogger = logging.getLogger(__name__)


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_profile(request, usrname):
    user = get_object_or_404(User, username=usrname)

    # get details of a single profile
    if request.method == 'GET':
        stdlogger.info("API_get : request for profile '" + usrname + "' retrieval")
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # delete a single profile
    elif request.method == 'DELETE':
        stdlogger.info("API_delete : request for profile '" + usrname + "' deletion")
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of a single profile
    elif request.method == 'PUT':
        stdlogger.info("API_put : request for profile '" + usrname + "' update")
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # data received is valid
            stdlogger.debug("API_put : data for update has been successfully validated")
            serializer.save()
            stdlogger.info("API_post : the profile for '" + serializer.data['username'] + "' has been updated")
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        else:
            # data received is invalid
            stdlogger.error("API_put : data for update has not been validated")
            for field, errors in serializer.errors.items():
                for error in errors:
                    stdlogger.error(field + " -> " + error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_profiles(request):
    # get all profiles
    if request.method == 'GET':
        stdlogger.info("API_get_all : request for all profiles retrieval")
        people = User.objects.all()
        serializer = UserSerializer(people, many=True)
        return Response(serializer.data)

    # insert a new record for a profile
    elif request.method == 'POST':
        stdlogger.info("API_post : request for single profile creation")
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # data received is valid
            stdlogger.debug("API_post : data for new profile has been successfully validated")
            serializer.save()
            stdlogger.info("API_post : new profile for '" + serializer.data['username'] + "' has been created")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            # data received is invalid
            stdlogger.error("API_post : data for new profile has not been validated")
            for field, errors in serializer.errors.items():
                for error in errors:
                    stdlogger.error(field + " -> " + error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
