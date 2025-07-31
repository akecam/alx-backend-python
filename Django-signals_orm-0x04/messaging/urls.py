from django.urls import path
from .views import MessageListCreateView, MessageDetailsView

urlpatterns = [
    path('message/', MessageListCreateView.as_view(), name="message"),
    path('message/<uuid:pk>', MessageDetailsView.as_view(), name="message-detail")
]