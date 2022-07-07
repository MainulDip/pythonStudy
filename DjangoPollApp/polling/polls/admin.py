from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# admin.site.register([Question, Choice])
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline): # admin.StackedInline for vertical listing
    model = Choice
    extra = 0 # how many extra row after lisitng all options
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    
    # fieldsets accept tuple
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.site_header = "Polls Admin Header"
admin.site.site_title = "title Polls"
admin.site.index_title = "Welocome Admin From index_title"
