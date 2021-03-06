from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1



class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text'] # 필드의 순서를 바꾼다.
    fieldsets = [
        ( None , {'fields' : ['question_text']}),
        ('Date Information',{'fields' : ['pub_date'],'classes' : ['collapse']}),

    ]
    inlines = [ChoiceInline]
    list_display=('question_text','pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
