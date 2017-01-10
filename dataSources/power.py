from .util import call, search_percent

def get():
    out = call('acpi')
    #TODO figure out more acpi outputs
    return ' ' + search_percent(out)
