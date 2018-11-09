import requests as req

def download(URL, LOC=None):
    if LOC == None:
        LOC = URL.split('/')[-1]
    r = req.get(URL, allow_redirects=True)
    with open(LOC, 'w') as file:
        file.write(bytes.decode(r.content, 'utf8'))
    return LOC

LOC = download(input('URL:> '))
cmdexec('path -a ' + LOC)
