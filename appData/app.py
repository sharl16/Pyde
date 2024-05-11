import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from appData import interpeter
from appData import misc
from appData.highlighter import highlight_keywords  

global current_file_object
global file_path

#menu bar commands:
def mbar_file_open(event=None):
    global file_path 
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Python Files", "*.py"), ("All files", "*.*")])
    if file_path:
        process_file(file_path)

def mbar_file_new(event=None):
    global file_path
    file_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:
        create_file(file_path)
        run_script.config(state="normal")
        close_button.config(state="normal")
    

def mbar_help_about():
    misc.display_about()

def change_theme():
    theme.set(1)

#file processing (saving, opening, closing)
def process_file(file_path):
    global current_file_object
    try:
        current_file_object = open(file_path, 'r', encoding='utf-8')
        file_contents = current_file_object.read()
        #current_file = file_contents
        file_text.delete('1.0', tk.END)
        file_text.insert(tk.END, file_contents)
        run_script.config(state="normal")
        close_button.config(state="normal")
        edit_menu.entryconfig(0, state=tk.NORMAL) # enables the "Run" option at the menu bar
        selected_file_label.config(text=f"Selected File: {file_path}")
        highlight_keywords(file_text)  # for syntax highlighting
    except UnicodeDecodeError:
        messagebox.showerror("Sorry!", "A UnicodeDecodeError occured when trying to read the file. File might contain binary data.")
    except TimeoutError:
        messagebox.showerror("Sorry!", "A TimeoutError occured when trying to read the file. It could be caused by low memory. Try restarting your computer")
    except Exception as e:
        messagebox.showerror("Sorry!", str(e))

def create_file(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as new_file:
            new_file.write("#Visit Python Docs to get started as a beginner, https://docs.python.org/3/.\n#Visit Pyde GitHub Page for more information on Pyde, https://github.com/sharl16/Pyde.\n#You can disable this message in Settings.")
        process_file(file_path)
    except Exception as e:
        messagebox.showerror("Sorry!", str(e))

def save_file():
    global file_path
    try:
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_text.get('1.0', tk.END))
        else:
            messagebox.showerror("Sorry!", "Could not find a active file to save.")
    except Exception as e:
        messagebox.showerror("Sorry!", str(e))

def close_file():
    global current_file_object
    if current_file_object:
        save_prompt = messagebox.askyesnocancel("Save File", "Do you want to save changes before closing?")
        if save_prompt is None: #user canceled
            return
        elif save_prompt:
            save_file()
        current_file_object.close()
        file_text.delete('1.0', tk.END)
        selected_file_label.config(text=f"")
        run_script.config(state="disabled")
        close_button.config(state="disabled")

#code processing
def receive_output(output):
    print(output)
    terminal_text.insert(tk.END, output)

def send_code():
    code = file_text.get("1.0", tk.END) 
    output = interpeter.run_python(code) # thats the bit that actually runs the code
    receive_output(output) 

#base window
root = tk.Tk()
root.title("Pyde v1.0.4")
root.geometry("1280x720")
appIcon = r'_internal\appData\resources\pydeIcon.ico'
root.iconbitmap(appIcon)
menubar = tk.Menu()
theme = tk.IntVar()
theme.set(0) #default (dark)
root.configure(bg="#181818")
#root.overrideredirect(True)
#menu bar widgets
file_menu = tk.Menu(menubar, tearoff=False)
about_menu = tk.Menu(menubar, tearoff=False)
edit_menu = tk.Menu(menubar, tearoff=False)
settings_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(
    label="Open File",
    accelerator="Ctrl+O",
    command=mbar_file_open
)
file_menu.add_command(
    label="New File",
    accelerator="Ctrl+N",
    command=mbar_file_new
)
about_menu.add_command(
    label="About",
    accelerator="",
    command=mbar_help_about
)
edit_menu.add_command(
    label="Run",
    accelerator="F5",
    command=send_code,
    state=tk.DISABLED
)
edit_menu.add_command(
    label="Configure Interpeter",
    accelerator="",
    command=print("Not implemented"),
    state=tk.DISABLED
)
edit_menu.add_command(
    label="Add Interpeter",
    accelerator="",
    command=print("Not implemented"),
    state=tk.DISABLED
)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
theme_menu = tk.Menu(menubar, tearoff=False)
theme_menu.add_radiobutton(
    label="Light",
    variable=theme,
    value=1,
    command=change_theme
)
theme_menu.add_radiobutton(
    label="Dark",
    value=2,
    variable=theme,
    command=change_theme,
    state=tk.DISABLED
)

#add widgets to menu bar
root.bind_all("<Control-o>", mbar_file_open)
root.bind_all("<Control-O>", mbar_file_open)
root.bind_all("<Control-n>", mbar_file_new)
root.bind_all("<Control-N>", mbar_file_new)
root.bind_all("<F5>", send_code)
menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=edit_menu, label="Edit")
menubar.add_cascade(menu=settings_menu, label="Settings")
menubar.add_cascade(menu=about_menu, label="Help")
settings_menu.add_cascade(menu=theme_menu, label="Theme")
#rest of window
selected_file_label = tk.Label(root, text="")
selected_file_label.configure(bg="#181818", fg="white")
selected_file_label.pack()
close_button = tk.Button(root, text="Close File", command=close_file, state="disabled", bg="#242424", fg="white")
close_button.place(x=85,y=3.5,width=90,height=25)
run_script = tk.Button(root, text="Run", command=send_code, state="disabled", bg="#242424", fg="white")
run_script.place(x=20, y=3.5, width=60, height=25)
file_text = tk.Text(root, wrap=tk.WORD)
file_text.place(x=20, y= 35,width=1875, height=720)
file_text.configure(bg="#1f1f1f", fg="white")
#file_text.configure(text="white")
#terminal
terminal_text = tk.Text(root, wrap=tk.WORD)
terminal_text.configure(bg="#1f1f1f", fg="white")
terminal_text.place(x=20, y= 770,width=1875, height=225)
#tkinter window creation
file_text.bind("<KeyRelease>", lambda event: highlight_keywords(file_text))
root.config(menu=menubar)
def start_app():
    root.mainloop()
