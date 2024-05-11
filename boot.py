import tkinter as tk

def show_splash(image_path, window_width, window_height):
    global splash_root
    splash_root = tk.Tk()
    splash_root.image = tk.PhotoImage(file=image_path)
    global label
    label = tk.Label(splash_root, image=splash_root.image, bg='white')
    label.image = splash_root.image
    splash_root.overrideredirect(True)
    splash_root.lift()
    splash_root.wm_attributes("-topmost", True)
    splash_root.wm_attributes("-disabled", True)
    splash_root.wm_attributes("-transparentcolor", "white")

    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    splash_root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    label.pack()
    splash_root.after(4000, lambda: splash_root.destroy())
    splash_root.mainloop()

image_path = r'_internal\appData\resources\PydeSplash.png'
window_width = 600
window_height = 282

show_splash(image_path,window_width,window_height)
from appData import app
app.start_app()



