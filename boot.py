import tkinter as tk
import app

def show_splash(image_path, window_width, window_height):
    global root
    root = tk.Tk()
    root.image = tk.PhotoImage(file=image_path)
    global label
    label = tk.Label(root, image=root.image, bg='white')
    label.image = root.image
    root.overrideredirect(True)
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    label.pack()
    root.after(4000, lambda: root.destroy())
    root.mainloop()

image_path = r'resources\PydeSplash.png'
window_width = 600
window_height = 282

show_splash(image_path,window_width,window_height)
app.show_window()



