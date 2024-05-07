import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import TclError

def highlight_keywords(text_widget):
    try:
        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)

        cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

        # These five lines are optional. If omitted, default colours are used.
        cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
        cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
        cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

        ip.Percolator(text_widget).insertfilter(cdg)
    except TclError:
        # Handle the case when the redirection already exists
        pass
