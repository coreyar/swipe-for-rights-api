from apistar import annotate

def public(*args, **kwargs):
    """Public API endpoint.

    This un-requires authentication by setting ``permissions`` to an empty list.
    ``permissions`` can still be passed in as a ``kwarg``.
    """
    permissions = kwargs.pop('permissions', [])
    return annotate(
        *args,
        permissions=[*permissions],
        **kwargs
    )
