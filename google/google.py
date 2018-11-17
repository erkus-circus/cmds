import webbrowser as wbb
from sys import argv
if len(argv) < 2:
    argv = [1,'']
wbb.get().open_new_tab('https://www.google.com/search?q=' + '%20'.join(argv[1:]))