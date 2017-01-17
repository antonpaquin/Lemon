from .util import call
import re

def get():
    out = call('netctl list')
    '''
    (?<=^\* ).*?$
        (?<=^\* )
            match a "* " at the beginning of a line (positive lookbehind)
        .*?$
            match anything, non-greedily until the end of the line
    '''

    reg = re.search('(?<=^\* ).*?$', out, flags=re.MULTILINE)
    try:
        wName = reg.group(0)
    except Exception:
        wName = 'None'
    return ' ' + wName
