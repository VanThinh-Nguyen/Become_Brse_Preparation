from django.urls import path
from .views import sse_view,send_message

urlpatterns = [
    path('sse/', sse_view, name='sse'),
    path('send/',send_message)
]
