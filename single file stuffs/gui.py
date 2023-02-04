import tkinter as tk
from math import sqrt

window=tk.Tk()

window.title("My first GUI")
window.geometry("500x500")  



def callback_button_reset():
    ent_a.delete(0, tk.END)
    ent_b.delete(0, tk.END)
    ent_c.configure(state="normal")
    ent_c.delete(0, tk.END)
    ent_c.configure(state="disabled")
    print("reset")

def open_popup(text):
    popup = tk.Tk()
    popup.geometry("10x100")
    popup.title("error")
    label = tk.Label(popup, text=text)
    label.pack()
    btn_close = tk.Button(master=popup, text="close", height= 1, command= popup.destroy) 
    btn_close.pack()

    popup.mainloop()


def callback_button_calculate():
    a = ent_a.get()
    b = ent_b.get()
    try: a = float(a);
    except ValueError:
        open_popup("a is not a number")
        return
    try: b = float(b)
    except ValueError:
        open_popup("b is not a number")
        return
    c = sqrt((a * a) + (b * b))
    ent_c.configure(state="normal")
    ent_c.delete(0,tk.END)
    ent_c.insert(0,c)
    ent_c.configure(state="disabled")
    print("calculate")

## make the objects
txt_title = tk.Label(master=window, 
                    text="pythaoras formula calculator",
                    font=("Arial", 20),)

txt_a = tk.Label(master=window,text="a = ")
ent_a = tk.Entry(master=window)
txt_b = tk.Label(master=window,text="b = ")
ent_b = tk.Entry(master=window)
txt_c = tk.Label(master=window,text="c = ")
ent_c = tk.Entry(master=window, bg="grey", state="disabled")

btn_calculate = tk.Button(master=window, text="calculate",bg="green" , height= 3, command=callback_button_calculate)
btn_reset = tk.Button(master=window, text="reset",bg="orange", height= 3, command= callback_button_reset)
btn_quit = tk.Button(master=window, text="quit",  bg="tomato", height= 3, command=window.quit)

## place them on the grid
txt_title.grid(row=0, column=0, columnspan=6)

txt_a.grid(row=1, column=0, sticky=tk.EW)
ent_a.grid(row=1, column=1)
txt_b.grid(row=1, column=2, sticky=tk.EW)
ent_b.grid(row=1, column=3)
txt_c.grid(row=1, column=4, sticky=tk.EW)
ent_c.grid(row=1, column=5)

btn_calculate.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=tk.EW)
btn_reset.grid(row=2, column=2, columnspan=2, rowspan=2, sticky=tk.EW)
btn_quit.grid(row=2, column=4, columnspan=2, rowspan=2, sticky=tk.EW)




##always at the end
window.mainloop()



