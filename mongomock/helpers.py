from functools import wraps
import re

try:
    from bson import (ObjectId, RE_TYPE)
except ImportError:
    from mongomock.object_id import ObjectId
    RE_TYPE = type(re.compile(''))

import logging
log = logging.getLogger(__name__)
import log as log_helpers

log_helpers.enable_pretty_logging('INFO', log)

#for Python 3 compatibility
try:
  unicode = unicode
  from __builtin__ import basestring
except NameError:
  unicode = str
  basestring = (str, bytes)

def _fields_list_to_dict(fields):
    """Takes a list of field names and returns a matching dictionary.

    ["a", "b"] becomes {"a": 1, "b": 1}

    and

    ["a.b.c", "d", "a.c"] becomes {"a.b.c": 1, "d": 1, "a.c": 1}
    """
    as_dict = {}
    for field in fields:
        if not isinstance(field, basestring):
            raise TypeError("fields must be a list of key names, "
                            "each an instance of %s" % (basestring.__name__,))
        as_dict[field] = 1
    return as_dict

def mimic_async(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        callback = kwargs.pop('callback', None)
        if callback:
            try:
                log.debug("Async-Calling cb %s with a:%s, k:%s", func, args, kwargs)
                result = func(*args, **kwargs)
                callback((result, None))
            except Exception, e:
                log.error("Caught exception %s", e, exc_info=True)
                callback((None, e))
        else:
            log.debug("Calling %s with a:%s, k:%s", func, args, kwargs)
            return func(*args, **kwargs)
    return wrapper

def mimic_async_cls(cls):
    for attr, val in cls.__dict__.iteritems(): # there's propably a better way to do this
        if callable(val) and not attr.startswith('_'):
            setattr(cls, attr, mimic_async(val))
    return cls
