from django.contrib import admin

# Register your models here.
from .models import StudentInfo, LanguageDisability, MathematicalDisability, ParentalMetric


# # 9 Set up the Choice options on the Question page
# # extra = 3 says to provide 3 extra choice options by
# # default
#
# # 9.a Change StackedInline to TabularInline to
# # take up less space
#
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# # 7 You can change the order of how items show up
# # like this
#
# class QuestionAdmin(admin.ModelAdmin):
#     # 7 fields = ['pub_date', 'question_text']
#
#     # 8 You can also break up the data in blocks
#     ''' 9 Add choices to Question page
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date Information', {'fields': ['pub_date']}),
#     ]
#     '''
#
#     # 9 Updated fieldsets
#     # collapse collapses a field by default
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
#     # 10 Change the Question list page to display the
#     # date published and whether it is recent
#
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#
#     # 11 Over to polls/models.py to fix was_published_recently
#
#     # 14 Add a filter box that lets the user sort by
#     # pub_date
#     list_filter = ['pub_date']
#
#     # 14 Allow the user to search by question text
#     search_fields = ['question_text']
#
#     # 15 Over to sampsite/settings.py to change the page title
#
# # admin.site.register(Question)
# admin.site.register(Question, QuestionAdmin)

class MathematicalDisabilityAdmin(admin.ModelAdmin):
    fields = ['disability_name', ]
    list_display = ['disability_name', ]

class LanguageDisabilityAdmin(admin.ModelAdmin):
    fields = ['disability_name', ]
    list_display = ['disability_name', ]

class ParentalMetricAdmin(admin.ModelAdmin):
    fields = ['metric_name', ]
    list_display = ['metric_name', ]


admin.site.register(MathematicalDisability, MathematicalDisabilityAdmin)
admin.site.register(LanguageDisability, LanguageDisabilityAdmin)
admin.site.register(ParentalMetric, ParentalMetricAdmin)