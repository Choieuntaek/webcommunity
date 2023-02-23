from django.shortcuts import render
import datetime
from django.utils import timezone
# Create your views here.
from sell.models import Category, Writing


def index(request):
    category = Category.objects.all()
    writing_list_day = Writing.objects.filter(create_date__gte=timezone.now() - datetime.timedelta(hours=24)).order_by(
        '-view')
    writing_list_week = Writing.objects.filter(create_date__gte=timezone.now() - datetime.timedelta(days=7)).order_by(
        '-view')
    writing_list_month = Writing.objects.filter(create_date__gte=timezone.now() - datetime.timedelta(days=30)).order_by(
        '-view')
    writing_notice = Writing.objects.filter(category=1).order_by('-create_date')

    context = {'category': category,
               'writing_list_day': writing_list_day, 'writing_list_week': writing_list_week,
               'writing_list_month': writing_list_month,
               'writing_notice': writing_notice}

    return render(request, 'main.html', context)
