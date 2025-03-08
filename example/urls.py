from django.urls import path
from .views import index  # Import your view function

urlpatterns = [
    path('', index, name='index_page'),  # Ensure name matches what is used in the template
]
