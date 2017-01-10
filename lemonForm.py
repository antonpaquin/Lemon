def highlight(inner):
    return '%{R}' + inner + '%{R}'

def leftAlign(inner):
    return '%{l}' + inner

def centerAlign(inner):
    return '%{c}' + inner

def rightAlign(inner):
    return '%{r}' + inner

def font(inner, fontIndex):
    return '%{T' + str(fontIndex) + '}' + inner + '%{T-}'

def background(inner, color):
    return '%{B'+color+'}' + inner + '%{B-}'

def foreground(inner, color):
    return '%{F'+color+'}' + inner + '%{F-}'

def underline(inner, color):
    return '%{U'+color+'}%{+u}' + inner + '%{-u}%{U-}'

def buttonLeft(inner, command):
    return '%{A:'+command+':}' + inner + '%{A}'

def buttonRight(inner, command):
    return '%{A3:'+command+':}' + inner + '%{A}'
