_callbacks = {}


def register(func, hook, order: int = 0):
    def register_callback(func):
        return func

    return register_callback
