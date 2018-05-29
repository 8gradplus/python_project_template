from functools import wraps


class on_enter:

    def __init__(self, g):
        self.g = g

    def __call__(self, f):
        @wraps(f)
        def closure(*args, **kwargs):
            self.g(str(args) + str(kwargs))
            return f(*args, **kwargs)
        return closure


class on_exit:

    def __init__(self, g):
        self.g = g

    def __call__(self, f):
        @wraps(f)
        def closure(*args, **kwargs):
            result = f(*args, **kwargs)
            self.g(str(args) + str(kwargs))
            return result
        return closure
