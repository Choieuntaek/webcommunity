from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sell.forms import CommentForm
# Create your views here.
from sell.models import Writing, Comment


@login_required(login_url='account_login')
def comment_create(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        level = request.POST['level']
        if form.is_valid():
            if level == '0':
                comment = form.save(commit=False)
                comment.author = request.user
                comment.create_date = timezone.now()
                comment.writing = writing
                comment.save()
                comment.reply_id = comment.id
                comment.save()
            else:
                comment = form.save(commit=False)
                comment.author = request.user
                comment.create_date = timezone.now()
                comment.writing = writing
                comment.save()
            return redirect('sell:writing_detail', writing_id=writing.id)

    else:
        form = CommentForm()
    context = {'writing': writing, 'form': form}
    return render(request, 'writing_detail.html', context)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return redirect('sell:writing_detail', writing_id=comment.writing.id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.reply_id = comment.id
            comment.save()
            return redirect('sell:writing_detail', writing_id=comment.writing.id)
    else:
        comment_form = CommentForm(instance=comment)
    context = {'comment': comment, 'comment_form': comment_form}
    return render(request, 'writing_detail.html', context)

@login_required(login_url='account_login')
def comment_delete(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return redirect('sell:writing_detail', writing_id=comment.writing.id)
    comment.id = comment_id
    comment.reply_id = comment.reply_id
    comment.level = comment.level
    comment.deleted = True
    comment.save()
    return redirect('sell:writing_detail', writing_id=comment.writing.id)

