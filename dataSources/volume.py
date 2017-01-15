from .util import call, search_percent

def get():
    out = call('amixer -M sget \'Master\'')
    return ' ' + search_percent(out)
