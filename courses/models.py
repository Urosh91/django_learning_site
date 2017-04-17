from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import math

STAUS_CHOICE = (
    ('i', 'In Progress'),
    ('r', 'In review'),
    ('p', 'Published'),
)


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User)
    subject = models.CharField(default='', max_length=100)
    status = models.CharField(max_length=1, choices=STAUS_CHOICE, default='i')

    def __str__(self):
        return self.title

    def time_to_complete(self):
        from courses.templatetags import course_extras
        return f'{course_extras.time_estimate(len(self.description.split()))} min.'


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        abstract = True
        ordering = ['-order',]
        # They'll be ordered by id, as default is set to 0

    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.pk
        })


class Quiz(Step):
    total_questions = models.IntegerField(default=4)

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.pk
        })

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order',]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt


class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)


class TrueFalseQuestion(Question):
    pass


class Answer(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.text