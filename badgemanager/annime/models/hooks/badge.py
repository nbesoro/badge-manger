from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from annime.models import AnnimeVideo


def starter(sender, instance, created=False, update_fields=None, **kwargs):
    if update_fields and "number_of_views" in update_fields:
        instance.refresh_from_db()
        if instance.number_of_views >= 1000:
            instance.author.has_starter = True
            instance.author.save(update_fields=["has_starter"])

    elif created:
        author_video_number = AnnimeVideo.objects.filter(author=instance.author).count()
        if author_video_number >= 5:
            instance.author.has_collector = True
            instance.author.save(update_fields=["has_collector"])


@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    print("User logged in", user)
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    if user.date_joined <= one_year_ago:
        user.has_pionner = True
        user.save(update_fields=["has_pionner"])


post_save.connect(starter, sender=AnnimeVideo)
