from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import F
from django.urls import reverse

from .forms import CommentForm
from .models import Comment


def home(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            print('KAIF')
            return HttpResponseRedirect(reverse('home'))
    comments = Comment.objects.all().order_by('-id')
    context = {"comments": comments, 'form': CommentForm()}
    return render(request, "index.html", context)
