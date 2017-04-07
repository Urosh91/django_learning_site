from django.http import HttpResponse
from django.shortcuts import render

from . import models


def course_list(request):
    courses = models.Course.objects.all()
    output = ', '.join(str(course) for course in courses)
    return HttpResponse(output)

