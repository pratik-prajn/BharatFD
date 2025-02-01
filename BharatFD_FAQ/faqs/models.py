from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from langdetect import detect
from django.utils.html import strip_tags

class FAQ(models.Model):
    question = models.TextField()
    question_lang = models.CharField(max_length=10, blank=True, null=True)  
    translated_question = models.TextField(blank=True, null=True)           
    answer = RichTextField()
    answer_lang = models.CharField(max_length=10, blank=True, null=True)     
    translated_answer = models.TextField(blank=True, null=True)              

    def save(self, *args, **kwargs):
        translator = Translator()
        
        # Process question
        detected_q_lang = detect(self.question)
        self.question_lang = detected_q_lang
        if detected_q_lang != 'en':
            self.translated_question = translator.translate(self.question, dest='en').text
        else:
            self.translated_question = self.question
        
        
        plain_answer = strip_tags(self.answer)
        detected_a_lang = detect(plain_answer)
        self.answer_lang = detected_a_lang
        if detected_a_lang != 'en':
            self.translated_answer = translator.translate(plain_answer, dest='en').text
        else:
            self.translated_answer = plain_answer

        super().save(*args, **kwargs)

    @property
    def plain_answer(self):
        """Return answer without HTML tags."""
        return strip_tags(self.answer)

    def __str__(self):
        
        return self.translated_question or self.question
