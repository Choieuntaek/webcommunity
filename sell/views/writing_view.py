from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from sell.forms import WritingForm
from sell.models import Category
from sell.models import Writing, Comment, Writingip


def writing_list(request, category_name):

    category = Category.objects.get(title=category_name)
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')

    if so == 'comment':
        writing_list = Writing.objects.filter(category=category).annotate(num_comment=Count('comment')).order_by('-num_comment','-create_date')
    elif so == 'views':
        writing_list = Writing.objects.filter(category=category).order_by('-view', '-create_date')
    elif so == 'recent':
        writing_list = Writing.objects.filter(category=category).order_by('-create_date')
    else:
        writing_list = Writing.objects.filter(category=category).order_by('-create_date')

    if kw:
        writing_list = writing_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)  # 내용 검색
        ).distinct()

    paginator = Paginator(writing_list, 15)
    page_obj = paginator.get_page(page)
    context = {'writing_list': page_obj, 'category': category, 'page':page, 'kw':kw, 'so':so}

    return render(request, 'writing_list.html', context)

def writing_detail(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)

    ip = get_client_ip(request)
    cnt = Writingip.objects.filter(ip=ip, writing=writing).count()
    if cnt == 0:
        qc = Writingip(ip=ip, writing=writing)
        qc.save()
        if writing.view:
            writing.view += 1
        else:
            writing.view = 1
        writing.save()

    comment = Comment.objects.filter(writing__id=writing_id).order_by('reply_id','level','id')
    context = {'writing': writing, 'comment': comment}

    return render(request, 'writing_detail.html', context)

@login_required(login_url='account_login')
def writing_create(request, category_name):
    category = Category.objects.get(title=category_name)
    if category.level == 0:
        if request.user.level == 0:
            if request.method == 'POST':
                form = WritingForm(request.POST)
                if form.is_valid():
                    writing = form.save(commit=False)
                    writing.author = request.user
                    writing.category = category
                    writing.is_new = True
                    writing.create_date = timezone.now()
                    writing.save()
                    return redirect('sell:writing_detail', writing_id=writing.id)
            else:
                form = WritingForm()
            context = {'form': form, 'category': category}

            return render(request, 'writing_form.html', context)
        else:
            return redirect('sell:writing_list', category_name=category.title)
    else:
        if request.method == 'POST':
            form = WritingForm(request.POST)
            if form.is_valid():
                writing = form.save(commit=False)
                writing.author = request.user
                writing.category = category
                writing.is_new = True
                writing.create_date = timezone.now()
                writing.save()
                return redirect('sell:writing_detail', writing_id=writing.id)
        else:
            form = WritingForm()
        context = {'form': form, 'category': category}

        return render(request, 'writing_form.html', context)


@login_required(login_url='account_login')
def writing_modify(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    category = writing.category
    if request.user != writing.author:
        return redirect('sell:writing_detail', writing_id=writing.id)

    if request.method == 'POST':
        form = WritingForm(request.POST, instance=writing)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.author = request.user
            writing.modify_date = timezone.now()
            writing.save()
            return redirect('sell:writing_detail', writing_id=writing.id)
    else:
        form = WritingForm(instance=writing)
    context = {'writing': writing, 'form': form, 'category':category}
    return render(request, 'writing_form.html', context)


@login_required(login_url='account_login')
def writing_delete(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    if request.user != writing.author:
        return redirect('sell:writing_detail', writing_id=writing.id)
    writing.delete()
    return redirect('sell:writing_list', category_name=writing.category.title)

def get_client_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
    ip = x_forwarded_for.split(',')[-1].strip()
  else:
    ip = request.META.get('REMOTE_ADDR')
  return ip