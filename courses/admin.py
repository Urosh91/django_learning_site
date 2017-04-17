from django.contrib import admin
from datetime import date

from . import models


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

make_published.short_description = 'Mark selected courses as Published'


class TextInLine(admin.StackedInline):
    model = models.Text
    # This creates an inline, which we can then use


class QuizInLine(admin.StackedInline):
    model = models.Quiz


class AnswerInLine(admin.TabularInline):
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

    list_display = ['title', 'created_at', 'time_to_complete', 'status']

    list_editable = ['status']

    actions = [make_published]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine,]

    search_fields = ['prompt']

    list_display = ['prompt', 'quiz', 'order']

    list_editable = ['quiz', 'order']

    radio_fields = {'quiz': admin.HORIZONTAL}


class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']

    list_display = ['title', 'total_questions']

    actions = ['delete_selected']


class TextAdmin(admin.ModelAdmin):
    # fields = ['course', 'title', 'description', 'order', 'content']

    fieldsets = (
        (None, {'fields': (('course', 'title',), 'order', 'description')}),
        ('Add content', {'fields': ('content',), 'classes': ('collapse',)}),
    )

admin.site.register(models.Course, CourseAdmin)
# Register Course as CourseAdmin
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)
admin.site.disable_action('delete_selected')

