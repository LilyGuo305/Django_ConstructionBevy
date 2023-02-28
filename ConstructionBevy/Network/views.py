from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, ThreadModel, MessageModel
from .forms import PostForm, ThreadForm, MessageForm
from django.views.generic.edit import DeleteView
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'network/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'network/post_list.html', context)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'network/post_delete.html'
    success_url = reverse_lazy('post-list')

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        requestUser = request.user

        context = {
            'threads' : threads,
            'requestUser' : requestUser
        }

        return render(request, 'network/inbox.html', context)

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form' : form
        }
        return render(request, 'network/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)
            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()
                return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, '[Error] Invalid username, please try again.')
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'network/thread.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
        )

        message.save()
        return redirect('thread', pk=pk)

class DeleteThread(DeleteView):
    model = ThreadModel
    template_name = 'network/thread_delete.html'
    success_url = reverse_lazy('inbox')

class DeleteMessage(DeleteView):
    model = MessageModel
    template_name = 'network/message_delete.html'

    def get_success_url(self):
        pk = self.kwargs['inbox_pk']
        return reverse_lazy('thread', kwargs={'pk': pk})


