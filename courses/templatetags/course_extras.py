from django import template

from courses.models import Course


register = template.Library()


@register.simple_tag
def newest_course():
    '''Gets the latest course that was added to the library'''
    return Course.objects.latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses():
    '''Return dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}

# Inclusion tag returns a data as a whole other template, not just a string. So where ever this tag gets used it will
# include the given template also