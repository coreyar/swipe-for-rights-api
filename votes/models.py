from django.db import models


class Vote(models.Model):
    """A record of a User's support of a Bill"""
    # By id - we're not storing Bills yet
    bill_id: str = models.CharField('bill_id', max_length=32, unique=True)
    # True if they support, False if not
    supports: bool = models.BooleanField(default=False)
