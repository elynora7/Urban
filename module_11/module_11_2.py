import inspect
from pprint import pprint


class SomeClass:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 'Hello'


def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    result['attributes'] = vars(obj) if hasattr(obj, '__dict__') else {}
    result['methods'] = dir(obj)
    result['module'] = inspect.getmodule(obj)
    return result


some_obj = SomeClass()

# number_info = introspection_info(pprint)
number_info = introspection_info(some_obj)
pprint(number_info)


