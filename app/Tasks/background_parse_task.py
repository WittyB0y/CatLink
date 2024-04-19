from django.contrib.auth.models import User
from Link.models import Link
from utils.parser import extract_data_from_url
from CatApp.celery import celery


@celery.task
def parse_site(user_id, url):
    user = User.objects.get(id=user_id)
    data = extract_data_from_url(url)
    if isinstance(data, dict):
        Link.objects.create(
            user=user,
            title=data.get('title'),
            description=data.get('description'),
            image=data.get('image'),
            url=url,
            link_type=data.get('link_type')
        )


@celery.task
def parse_site_update(link_id, url):
    data = extract_data_from_url(url)
    if isinstance(data, dict):
        Link.objects.filter(id=link_id).update(
            title=data.get('title'),
            description=data.get('description'),
            image=data.get('image'),
            url=url,
            link_type=data.get('link_type')
        )
