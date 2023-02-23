from django.db.models.signals import post_save
from django.dispatch import receiver

from sell.models import Writing
from .webpush import release2_webpush


@receiver(post_save, sender=Writing)
def writing_post_save(sender, instance, created, **kwargs):
    if instance.category.title == 'release':
        if created:
            release2_webpush(instance)


from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from sell.models import Ip

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = set_ip(request)
    ip_list = Ip.objects.filter(user=user)
    for ip_info in ip_list:
        if ip_info.ip == ip:
            break
        else:
            Ip.objects.create(user=user, ip=ip)

def set_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        new_ip = x_forwarded_for.split(',')[-1].strip()
    else:
        new_ip = request.META.get('REMOTE_ADDR')
    return new_ip