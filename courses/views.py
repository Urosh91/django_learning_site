from django.shortcuts import render, get_object_or_404
from itertools import chain

from . import models


def course_list(request):
    courses = models.Course.objects.all()
    email = 'urosh43@gmail.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})
    # context dictionary


def course_detail(request, pk):
    # course = models.Course.objects.get(pk=pk)
    course = get_object_or_404(models.Course, pk=pk)
    # pk is ID by default
    # request comes in automatically and pk needs to be provided
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key = lambda step: step.order)
    return render(request, 'courses/course_detail.html', {'course': course, 'steps': steps})


def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/text_detail.html', {'step': step})


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/quiz_detail.html', {'step': step})

