import json

from webpush.utils import send_to_subscription

from sell.models import User
def release2_webpush(instance):

    users = User.objects.all()

    payload = {"head": " 달려~", "body": f"클릭하여 정보확인", "url": f"{instance.id}"}
    payload = json.dumps(payload)
    for user in users:
        push_infos = user.webpush_info.select_related("subscription")

        for push_info in push_infos:
            send_to_subscription(push_info.subscription, payload)

