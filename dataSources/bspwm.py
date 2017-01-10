from .util import call
import json

focused_color = '#CCC'
focused_background = '#555'

bspwm_colors = {
    'chromium-browser-chromium':'#88B6E1',
    'atom':'#5FB57D',
    'urxvt':'#2A357E',
    'unknown':'#555555',
    'none':'#333333'
}
def get():
    res = {}
    c = call('bspc query -T -d focused')
    if c == '':
        res['focused'] = '-1'
    else:
        desktop = json.loads(c)
        res['focused'] = desktop['name']
    for i in range(1,11):
        c = call('bspc query -T -n @'+str(i)+':')
        if c == '':
            res[i] = bspwm_colors['unknown']
            continue
        j = json.loads(c)
        try:
            name = j['client']['instanceName']
            if name in bspwm_colors.keys():
                res[i] = bspwm_colors[name]
            else:
                res[i] = bspwm_colors['unknown']
        except KeyError:
            res[i] = bspwm_colors['none']
    return res


def format(data, lemonForm):
    res = ''
    focused = int(data['focused'])
    for i in range(1,11):
        w = '   ' + str(i) + '   '
        #w = lemonForm.background(w, data[i])
        w = lemonForm.buttonLeft(w, 'bspc desktop -f ' + str(i))
        if i is focused:
            w = lemonForm.underline(w, focused_color)
        else:
            w = lemonForm.underline(w, data[i])
        res = res + w
    return res
