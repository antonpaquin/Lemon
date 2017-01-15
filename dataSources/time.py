from .util import call

def get():
    out = call('date').split(' ')
    res = {}
    res['day_of_week'] = out[0]
    res['month'] = out[1]
    res['day_of_month'] = out[2]
    t = out[3].split(':')
    res['hour'] = t[0]
    res['minute'] = t[1]
    res['second'] = t[2]
    res['year'] = out[5]
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
