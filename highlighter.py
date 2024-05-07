import tkinter as tk

def highlight_keywords(file_text):
    yellow_keywords = {
        "print",
        "function",
        "bind",
        "mainloop()",
        """"",
        """""
    }
    blue_keywords = {
        "def",
        "var",
        "not",
        "True",
        "False",
        "str",
        "int"
    }
    purple_keywords = {
        "import",
        "for",
        "while",
        "if",
        "break",
        "from",
        "(",
        ")"
    }
    
    text = file_text.get("1.0", "end")  
    # Clear all existing tags
    file_text.tag_remove("yellow_keyword", "1.0", "end")
    file_text.tag_remove("blue_keyword", "1.0", "end")
    file_text.tag_remove("purple_keyword", "1.0", "end")   
    # Highlight yellow keywords
    for keyword in yellow_keywords:
        start = "1.0"
        while True:
            pos = file_text.search(keyword, start, stopindex="end", nocase=True)
            if not pos:
                break
            start = pos + "+%dc" % len(keyword)
            file_text.tag_add("yellow_keyword", pos, start)
            file_text.tag_config("yellow_keyword", foreground="#ff983d")  # Custom RGB: Golden Yellow 
    # Highlight blue keywords
    for keyword in blue_keywords:
        start = "1.0"
        while True:
            pos = file_text.search(keyword, start, stopindex="end", nocase=True)
            if not pos:
                break
            start = pos + "+%dc" % len(keyword)
            file_text.tag_add("blue_keyword", pos, start)
            file_text.tag_config("blue_keyword", foreground="blue")
   
    # Highlight purple keywords
    for keyword in purple_keywords:
        start = "1.0"
        while True:
            pos = file_text.search(keyword, start, stopindex="end", nocase=True)
            if not pos:
                break
            start = pos + "+%dc" % len(keyword)
            file_text.tag_add("purple_keyword", pos, start)
            file_text.tag_config("purple_keyword", foreground="purple")
