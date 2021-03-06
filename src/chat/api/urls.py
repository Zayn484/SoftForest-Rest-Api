from django.urls import path
from .views import (
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    # ChatUpdateView,
    ChatDeleteView,
    GroupCreateView
)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    # path('<pk>/update/', ChatUpdateView.as_view()),
    path('delete/', ChatDeleteView.as_view()),
    path('group/create/', GroupCreateView.as_view()),
]