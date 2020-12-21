from celery import shared_task

from applications.blogs.models import Blog


@shared_task
def save_user_details(user_id, blog_id):
    Blog.objects.filter(id=blog_id).update(modified_by_id=user_id)
    print(" inside celery task")
