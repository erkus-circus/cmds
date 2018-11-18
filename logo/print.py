import base64 as b64
import webbrowser as wbb

with open('icon.gif','rb') as f:
       wbb.get().open_new_tab(b64.b64encode(f.read()))