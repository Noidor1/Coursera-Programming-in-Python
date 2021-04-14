import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = json.dumps(func(*args, **kwargs))
        return res
    return wrapper





