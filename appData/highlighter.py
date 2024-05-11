import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import TclError

def highlight_keywords(text_widget):
    try:
        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)

        cdg.tagdefs['MYGROUP'] = {'foreground': '#FFFFFF', 'background': '#1f1f1f'}

        cdg.tagdefs['COMMENT'] = {'foreground': '#999999', 'background': '#1f1f1f'}
        cdg.tagdefs['KEYWORD'] = {'foreground': '#C3E88D', 'background': '#1f1f1f'}
        cdg.tagdefs['BUILTIN'] = {'foreground': '#FFCB6B', 'background': '#1f1f1f'}
        cdg.tagdefs['STRING'] = {'foreground': '#FF5370', 'background': '#1f1f1f'}
        cdg.tagdefs['DEFINITION'] = {'foreground': '#82AAFF', 'background': '#1f1f1f'}

        ip.Percolator(text_widget).insertfilter(cdg)
    except TclError:
        pass

