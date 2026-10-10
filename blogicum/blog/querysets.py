from django.db import models
from django.utils.timezone import now


class PostQuerySet(models.QuerySet):
    def filter_published(self):
        return self.filter(
            is_published=True,
            pub_date__lte=now(),
            category__is_published=True,
        ).select_related(
            'author', 'category', 'location',
        )
