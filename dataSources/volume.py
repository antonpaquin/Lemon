from .util import call, search_percent

def get():
    out = call('amixer')
    return ' ' + search_percent(out)
