import requests
from onesignal import OneSignal, SegmentNotification

client = OneSignal('2f8579b9-55c5-42d1-b2d7-2ac1bafa6bdb',
                   'YzQ3NjU0NTYtYzk0Yy00YjJjLWE0MjUtOTAxOGI0Nzg3ZDE5')

notification_to_all_active_users = SegmentNotification(
    # template_id='7b5c5129-9018-4942-8943-d8674c42e2a0',
    subtitle={
        "en": "Kiss :kissing_heart:",
        "id": "Kiss :kissing_heart:",
    },
    contents={
        "en": "I Love U :heart:",
        "id": "I Love U :heart:",
    },
    included_segments=SegmentNotification.ACTIVE_USERS,
    big_picture="http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg",
    chrome_big_picture="http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg",
    url="http://1.bp.blogspot.com/-DrAN0RunYAY/Vdf3pIgDWeI/AAAAAAAAGxs/yw0JCoKD0Xc/s1600/gambar%2Blucu%2B%252818%2529.jpg",
)
client.send(notification_to_all_active_users)
