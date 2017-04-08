from django.shortcuts import render, get_object_or_404

from . import models


def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
    # context dictionary


def course_detail(request, pk):
    # course = models.Course.objects.get(pk=pk)
    course = get_object_or_404(models.Course, pk=pk)
    # pk is ID by default
    # request comes in automatically and pk needs to be provided
    return render(request, 'courses/course_detail.html', {'course': course})

