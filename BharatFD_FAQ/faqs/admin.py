from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'question_lang',
        'translated_question',
        'plain_answer',  
        'answer_lang',
        'translated_answer',
    )
    search_fields = ('question', 'translated_question', 'translated_answer')
    readonly_fields = ('question_lang', 'translated_question', 'answer_lang', 'translated_answer')
