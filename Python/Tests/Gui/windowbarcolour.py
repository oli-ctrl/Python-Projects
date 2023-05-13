## yoinked from (https://gist.github.com/Olikonsti/879edbf69b801d8519bf25e804cec0aa) THANKS SO MUCH

import ctypes as ct
import tkinter as tk

window= tk.Tk()

def makeDark(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))

window.title("Dark Title Bar")
makeDark(window)
window.geometry("400x400")
window.mainloop()