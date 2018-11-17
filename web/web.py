import webbrowser as wbb
from sys import argv
if len(argv) < 2:
    print('Usage: web <URL>')
else:
    wbb.get().open_new_tab(argv[1])