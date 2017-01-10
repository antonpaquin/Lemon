from .util import call

def get():
    out = call('date').split(' ')
    res = {}
    res['day_of_week'] = out[0]
    res['month'] = out[1]
    res['day_of_month'] = out[3]
    t = out[4].split(':')
    res['hour'] = t[0]
    res['minute'] = t[1]
    res['second'] = t[2]
    res['year'] = out[6]
    return res

def clock(data):
    return ' {}:{}'.format(
        data['hour'],
        data['minute']
    )

def date(data):
    return ' {} {} {}'.format(
        data['day_of_week'],
        data['month'],
        data['day_of_month']
    )
