from django.contrib import admin
from datetime import date

from . import models


class TextInLine(admin.StackedInline):
    model = models.Text
    # This creates an inline, which we can then use


class QuizInLine(admin.StackedInline):
    model = models.Quiz


class AnswerInLine(admin.StackedInline):
    model = models.Answer


class YearListFilter(admin.SimpleListFilter):
    title = 'year created'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (('2015','2015'),
                ('2016','2016')
                )

    # def search_year(self, queryset, value):
    #     if self.value() == value:
    #         return queryset.filter(created_at__gte=date(value, 1, 1),
    #                                created_at_lte=date(value, 12, 31))

    def queryset(self, request, queryset):
        if self.value() == '2015':
            return queryset.filter(created_at__gte=date(2015, 1, 1),
                                   created_at__lte=date(2015, 12, 31))

        if self.value() == '2016':
            return queryset.filter(created_at__gte=date(2016, 1, 1),
                                   created_at__lte=date(2016, 12, 31))


class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'subject', 'teacher']
    inlines = [TextInLine, QuizInLine]

    search_fields = ['title', 'description']

    list_filter = ['created_at', 'teacher', YearListFilter,]

    list_display = ['title', 'created_at']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine,]

    search_fields = ['prompt']

    list_display = ['prompt', 'quiz']


class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']

    list_display = ['title', 'total_questions']

admin.site.register(models.Course, CourseAdmin)
# Register Course as CourseAdmin
admin.site.register(models.Text)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)

