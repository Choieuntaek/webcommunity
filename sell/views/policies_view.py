from django.shortcuts import render

def user_agreement(request):

  return render(request, 'user_agreement.html')

def privacy_policy(request):
  return render(request, 'privacy_policy.html')