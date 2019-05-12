"""Utils module.

Bunch of useful functions.
"""
from bson import ObjectId


def to_dict(obj):
    """Am function to represent model as dict."""
    if not hasattr(obj, '__dict__'):
        return obj

    return dict(
        [
            (key, to_dict(value)) for key, value in obj.__dict__.items()
            if not callable(value) and key not in ['database', 'type'] and
            not key.startswith('_') and not isinstance(value, ObjectId)
        ])
