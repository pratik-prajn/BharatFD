import pytest
from django.urls import reverse
from faqs.models import FAQ  # Corrected import
from django.utils.html import strip_tags

@pytest.mark.django_db
def test_faq_list_api(client):
    # Create a sample FAQ instance.
    faq = FAQ.objects.create(
        question="<p>你吃了吗</p>",
        answer="<p>Have you eaten?</p>"
    )
    
    # Reverse URL using the name provided in your faqs/urls.py ("faq-list").
    url = reverse("faq-list")
    response = client.get(url, {"lang": "en"})
    data = response.json()

    # Ensure the response status is HTTP 200 OK.
    assert response.status_code == 200
    
    # Verify that the returned data includes the FAQ with HTML tags stripped.
    assert strip_tags(data[0]["question"]) == strip_tags(faq.get_translated_question("en"))
    assert strip_tags(data[0]["answer"]) == strip_tags(faq.answer)
    
    # Check that the detected language is present in the API response.
    assert "detected_lang" in data[0]
