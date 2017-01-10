import subprocess
import re

def call(command):
    return subprocess.Popen(command.split(' '), stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

def search_percent(sstr):
    return re.search('[0-9]{1,3}%', sstr).group(0)
