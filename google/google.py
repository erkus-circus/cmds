import webbrowser as wbb
from urllib import quote_plus

words = command.split()

if len(words) < 2:
    words = [1,'']

wbb.get().open_new_tab('https://www.google.com/search?q=' + quote_plus(words[1:]) + '&ie=UTF-8')
