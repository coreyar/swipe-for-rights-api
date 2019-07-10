import inspect
from django.db import models
from django.conf import settings


class UpdateMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CreateAndUpdateMixin(UpdateMixin):
    class Meta:
        abstract = True

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Choice(object):
    @classmethod
    def data(cls):
        if not getattr(cls, '_data', False):
            setattr(cls, '_data', [])

            members = inspect.getmembers(cls)
            for name, value in members:
                if not name.startswith('_') and not inspect.ismethod(value):
                    if isinstance(value, tuple) and len(value) > 1:
                        data = value
                    else:
                        pieces = [x.capitalize() for x in name.split('_')]
                        data = (value, ' '.join(pieces))
                    cls._data.append(data)
                    setattr(cls, name, data[0])

            cls._hash = dict(cls._data)
        return cls._data

    @classmethod
    def __len__(cls):
        return len(list(cls.data()))

    @classmethod
    def choices(cls):
        for value, data in cls.data():
            yield (value, data)

    @classmethod
    def max_length(cls):
        if not getattr(cls, '_max_length', False):
            max_length = 0
            for d in cls.data():
                max_length = max(len(str(d[0])), max_length)
            cls._max_length = max_length
        return cls._max_length

    @classmethod
    def get_value(cls, key):
        return cls._hash[key]


def user_based_path(instance, filename):
    if settings.TESTING:
        return filename
    if hasattr(instance, 'created_by'):
        id = instance.created_by.id
    else:
        id = instance.id
    return 'files/%i/%s' % (id, filename)
