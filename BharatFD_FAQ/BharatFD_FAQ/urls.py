from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_faqs(request):
    return redirect('/api/faqs/')  

urlpatterns = [
    path('', redirect_to_faqs),  # Redirect the empty path
    path('admin/', admin.site.urls),
    path('api/', include('faqs.urls')),
]
