from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_faqs(request):
    """
    Redirect only if the user is not accessing the admin panel.
    """
    if request.path == "/":
        return redirect('/admin/')  # Redirect root to admin panel
    return redirect('/api/faqs/')  # Otherwise, redirect to FAQs

urlpatterns = [
    path('', redirect_to_faqs),  # Redirect root to admin panel
    path('admin/', admin.site.urls),  # Admin panel remains accessible
    path('api/', include('faqs.urls')),  # Include FAQ API URLs
]
