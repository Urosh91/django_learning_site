from django.contrib import admin

from . import models


# class TextInLine(admin.StackedInline):
#     model = models.Text
#     # This creates an inline, which we can then use
#
#
# class QuizInLine(admin.StackedInline):
#     model = models.Quiz
#
#
# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInLine, QuizInLine]


admin.site.register(models.Course)
# Register Course as CourseAdmin
admin.site.register(models.Text)
admin.site.register(models.Quiz)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)
admin.site.register(models.Answer)

