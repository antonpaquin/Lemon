import lemonForm
import sys
from dataSources import bspwm as m_bspwm
from dataSources import cpu as m_cpu
from dataSources import power as m_power
from dataSources import time as m_time
from dataSources import volume as m_volume

from time import sleep
import threading

mainUpdateInterval = 0.05

getInfo = {
    'bspwm': m_bspwm.get,
    'cpu': m_cpu.get,
    'power': m_power.get,
    'time': m_time.get,
    'volume': m_volume.get
}

info = {
    'bspwm': getInfo['bspwm'](),
    'cpu': getInfo['cpu'](),
    'power': getInfo['power'](),
    'time': getInfo['time'](),
    'volume': getInfo['volume']()
}

delays = {
    'bspwm': 0.15,
    'cpu': 1,
    'power': 3,
    'time': 1,
    'volume': 0.5
}

def build():
    ' left center right'
    return ''.join([left(), center(), right()])

def left():
    ''
    return lemonForm.leftAlign('')

def center():
    'bspwm'
    return lemonForm.centerAlign(bspwm())

def right():
    'volume power cpu date time buffer'
    return lemonForm.rightAlign('  |  '.join([
        volume(),
        power(),
        cpu(),
        date(),
        clock() + '    '
    ]))


def bspwm():
    global info
    bspwm_i = info['bspwm']
    return m_bspwm.format(bspwm_i, lemonForm)

def volume():
    global info
    return info['volume']

def power():
    global info
    return info['power']

def cpu():
    global info
    return info['cpu']

def date():
    global info
    time_i = info['time']
    return m_time.date(time_i)

def clock():
    global info
    time_i = info['time']
    return m_time.clock(time_i)

def update_input(iname, delay):
    def f():
        global getInfo
        global info
        while(True):
            info[iname] = getInfo[iname]()
            sleep(delay)
    return f

for k in info.keys():
    t = threading.Thread(target=update_input(k, delays[k]))
    t.start()

while(True):
    print(build())
    sys.stdout.flush()
    sleep(mainUpdateInterval)
