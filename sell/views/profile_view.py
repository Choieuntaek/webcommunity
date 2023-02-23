from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from sell.models import Writing, Comment
from ..forms import ProfileUpdateForm, CheckPasswordForm


@login_required(login_url='account_login')
def profile(request):
    user = request.user
    writing = Writing.objects.filter(author=user).order_by("-create_date")
    comment = Comment.objects.filter(author=user).order_by("-create_date")

    context = {'writing': writing, 'comment':comment}
    return render(request, 'profile.html', context)

@login_required(login_url='account_login')
def profile_mcomment(request):
    user = request.user
    comment = Comment.objects.filter(author=user)
    writing_ids = set()
    for c in comment:
        if c.writing_id not in writing_ids:
            writing_ids.add(c.writing_id)
    writings = Writing.objects.filter(id__in=writing_ids).order_by("-create_date")
    context = {'writings': writings}
    return render(request, 'profile_mcomment.html', context)


@login_required(login_url='account_login')
def profile_update(request):

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user = form.save(commit=False)
            request.user.save()
            return redirect('sell:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'profile_update.html', context)


@login_required(login_url='account_login')
def profile_delete(request):

    if request.method == 'POST':
        form = CheckPasswordForm(request.user, request.POST)
        if form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('account_login')
    else:
        form = CheckPasswordForm(request.user)
    context = {'form': form}
    return render(request, 'profile_delete.html', context)