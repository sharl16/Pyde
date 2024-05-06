import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import interpeter

global current_file_object

#menu bar commands:
def mbar_file_open(event=None):
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Python Files", "*.py"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        process_file(file_path)

def mbar_file_new(event=None):
    file_path = filedialog.asksaveasfilename(title="Select Location", filetypes=[("Python Files", "*.py"), ("All files", "*.*")])

def mbar_help_about():
    messagebox.showinfo("About", "Pyde Tkinter\n""\nVersion 1.0")

def change_theme():
    print("changing themes is not implemented yet.")

#file processing (saving, opening, closing)
def process_file(file_path):
    global current_file_object
    try:
        run_script.config(state="normal")
        edit_menu.entryconfig(0, state=tk.NORMAL)
        #close_script.place(width=90, height=25)    
        #run_script.location(30,20)
        current_file_object = open(file_path, 'r', encoding='utf-8')
        file_contents = current_file_object.read()
        current_file = file_contents
        file_text.delete('1.0', tk.END)
        file_text.insert(tk.END, file_contents)
    except UnicodeDecodeError:
        messagebox.showerror("Error", "Unable to read the file. It may contain binary data.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_file():
    global file_path
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_text.get('1.0', tk.END))
    except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "No file is opened to save.")

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
        close_script.pack()
        run_script.pack()
        selected_file_label.config(text=f"")

#code processing
def receive_output(output):
    # Insert the output into the terminal text widget
    print(output)
    terminal_text.insert(tk.END, output)

def send_code():
    code = file_text.get("1.0", tk.END)  # Get the text from the Text widget
    output = interpeter.run_python(code)  # Pass the extracted text to the interpreter
    receive_output(output)  # Handle the output as needed

#base window
root = tk.Tk()
root.title("Pyde Tkinter")
root.geometry("1280x720")
menubar = tk.Menu()
theme = tk.IntVar()
theme.set(1) #default (light)
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
    command=print("Not implemented")
)
edit_menu.add_command(
    label="Add Interpeter",
    accelerator="",
    command=print("Not implemented")
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
menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=edit_menu, label="Edit")
menubar.add_cascade(menu=settings_menu, label="Settings")
menubar.add_cascade(menu=about_menu, label="Help")
settings_menu.add_cascade(menu=theme_menu, label="Theme")
#rest of window
close_script = tk.Button(root, text="Close file", command=close_file)
#close_script.place(width=90, height=25)
#close_script.pack_forget()
selected_file_label = tk.Label(root, text="")
selected_file_label.pack()
def open_terminal():
    terminal_window = tk.Toplevel(root)
    terminal_window.title("Terminal")
    # Add widgets and functionality to your terminal window here
terminal_button = tk.Button(root, text="Open Terminal", command=open_terminal)
terminal_button.place(x=85,y=3.5,width=90,height=25)
run_script = tk.Button(root, text="Run", command=send_code, state="disabled")
run_script.place(x=20, y=3.5, width=60, height=25)
file_text = tk.Text(root, wrap=tk.WORD)
file_text.place(x=20, y= 35,width=1875, height=720)
#terminal
terminal_text = tk.Text(root, wrap=tk.WORD)
terminal_text.place(x=20, y= 770,width=1875, height=225)
#tkinter window creation
root.config(menu=menubar)

def start_app():
    root.mainloop()
