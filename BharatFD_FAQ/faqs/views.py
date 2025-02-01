from django.core.cache import cache
from django.utils.html import strip_tags
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ

class FAQListAPIView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = [
            {
                "id": faq.id,
                # Translated question based on the requested language
                "question": strip_tags(faq.get_translated_question(lang)),
                # Original answer, stripped of HTML tags. You can also use get_translated_answer(lang) if needed.
                "answer": strip_tags(faq.answer),
                # Detected language for the question
                "detected_lang": faq.detected_lang,
                # English translation of the question (if exists)
                "translated_question": strip_tags(faq.question_en) if faq.question_en else strip_tags(faq.question),
                # English translation of the answer (if exists)
                "translated_answer": strip_tags(faq.answer_en) if faq.answer_en else strip_tags(faq.answer),
            }
            for faq in faqs
        ]

        cache.set(cache_key, data, timeout=3600)
        return Response(data)
