from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class choiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [choiceInline]
    

admin.site.register(Question, QuestionAdmin)

