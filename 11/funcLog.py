from time import time

def logged(when):
    def log(f, *args, **kargs):
        print('Called:')
        print('function:', f)
        print('args:', args)
        print('kargs:', kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print('time delta:', (time() - now))
        return wrapper

    try:
        return {'pre':pre_logged,
                'post':post_logged}[when]
    except KeyError as e:
        raise ValueError(e, 'must be "pre" or "post"')

@logged('post')
def hello(name):
    print('Hello,', name)

hello('World')
