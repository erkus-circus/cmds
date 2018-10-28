import webbrowser as wbb

words = command.split()

if len(words) < 2:
    words = [1,'']

wbb.get().open_new_tab('https://www.google.com/search?q=' + words[1:])
