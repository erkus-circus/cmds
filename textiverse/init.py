Ingame = True

def switch(var,obj):
    """equiv to js switch in python own wierd anoying way"""
    for i in obj:
        if var == i:
            return obj[i]
        else:
            try:
                return obj['default']
            except KeyError:
                return


while Ingame:
    