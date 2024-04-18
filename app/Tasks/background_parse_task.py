from django.contrib.auth.models import User
from Link.models import Link
from utils.parser import extract_data_from_url
from CatApp.celery import celery


@celery.task
def parse_site(user_id, link_type, url):
    user = User.objects.get(id=user_id)
    data = extract_data_from_url(url)
    link_type = 1 if link_type is None else link_type
    if isinstance(data, dict):
        Link.objects.create(
            user=user,
            title=data.get('title'),
            description=data.get('description'),
            image=data.get('image'),
            url=url,
            link_type=link_type
        )
