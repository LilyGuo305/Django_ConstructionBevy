from django.urls import path
from .views import PostListView, PostDeleteView, CreateThread, ListThreads, ThreadView, CreateMessage, DeleteThread

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
    path('inbox/delete/<int:pk>', DeleteThread.as_view(), name='delete-inbox')

]