from django.contrib import admin
from django import forms
from froala_editor.widgets import FroalaEditor
from django.utils.html import strip_tags
from .models import FAQ

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            # Use Froala editor for editing the question and answer fields.
            'question': FroalaEditor(options={'language': 'en'}),
            'answer': FroalaEditor(options={'language': 'en'}),
        }

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm

    # Use custom methods for list display so that plain text is shown
    list_display = ('plain_question', 'plain_question_en', 'plain_answer_en','detected_lang')
    
    # Readonly fields that show stripped versions
    readonly_fields = ('question_en','answer_en','detected_lang')

    def plain_question(self, obj):
        """Return the original question with HTML tags stripped."""
        return strip_tags(obj.question)
    plain_question.short_description = "Question"

    def plain_question_en(self, obj):
        """Return the English-translated question with HTML tags stripped."""
        return strip_tags(obj.question_en) if obj.question_en else ""
    plain_question_en.short_description = "Question (English)"

    def plain_answer_en(self, obj):
        """Return the English-translated answer with HTML tags stripped."""
        return strip_tags(obj.answer_en) if obj.answer_en else ""
    plain_answer_en.short_description = "Answer (English)"

admin.site.register(FAQ, FAQAdmin)
