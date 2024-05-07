import ctypes

#about dialog
shell32 = ctypes.windll.shell32

def display_about():
    shellabout = shell32.ShellAboutW
    shellabout.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_void_p]
    shellabout.restype = ctypes.c_int
    shellabout(None, "Pyde", "Version 1.0", None)
