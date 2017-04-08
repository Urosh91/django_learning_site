from django.contrib import admin

from . import models


class StepInLine(admin.StackedInline):
    model = models.Step
    # This creates an inline, which we can then use


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInLine,]


admin.site.register(models.Course, CourseAdmin)
# Register Course as CourseAdmin
admin.site.register(models.Step)
