from django.urls import path
from .views import home, save_text, get_texts, view_paste


urlpatterns = [
    path('', home),
    path('save_text', save_text),
    path('get_texts', get_texts),
    path('view_paste/<int:text_id>', view_paste),
]
