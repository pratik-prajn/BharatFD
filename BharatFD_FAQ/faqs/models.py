# faq/models.py
from django.db import models
from froala_editor.fields import FroalaField
from googletrans import Translator

class FAQ(models.Model):
    # Use Froala for both fields
    question = FroalaField(null=True, blank=True)  # Editable with Froala
    answer = FroalaField()  # Froala Editor for the answer

    detected_lang = models.CharField(max_length=10, null=True, blank=True)
    question_en = models.TextField(null=True, blank=True)
    answer_en = FroalaField(null=True, blank=True)  # English translation

    def save(self, *args, **kwargs):
        translator = Translator()
        # Detect the language of the question
        detected = translator.detect(self.question)
        self.detected_lang = detected.lang

        # Translate question to English if not already in English
        if self.detected_lang != "en" and not self.question_en:
            self.question_en = translator.translate(self.question, dest='en').text

        # Translate answer to English if not already in English
        if self.answer and self.detected_lang != "en" and not self.answer_en:
            self.answer_en = translator.translate(self.answer, dest='en').text

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

    def get_translated_question(self, lang):
        """
        Returns the translated question based on the requested language.
        If the requested language is English, return the English translation (if available);
        otherwise, fallback to the original question.
        """
        if lang == 'en':
            return self.question_en if self.question_en else self.question
        # For other languages, since no translations are defined,
        # you can return the original question or implement additional logic.
        return self.question

    def get_translated_answer(self, lang):
        """
        Returns the translated answer based on the requested language.
        For now, if language is 'en', return answer_en; otherwise, return the original answer.
        """
        if lang == 'en':
            return self.answer_en if self.answer_en else self.answer
        return self.answer
