import tkinter as tk
from math import sqrt

## init the window
window=tk.Tk()
window.title("Pythagoras calculator")
window.geometry("450x115")  


## what happens when the reset button is pressed
def callback_button_reset():
    ent_a.delete(0, tk.END)
    ent_b.delete(0, tk.END)
    ent_c.configure(state="normal")
    ent_c.delete(0, tk.END)
    ent_c.configure(state="disabled")

## what happens when the calculate button is pressed
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

## stuff for error popup window
def open_popup(text):
    popup = tk.Tk()
    popup.geometry("10x45")
    popup.title("error")
    label = tk.Label(popup, text=text)
    label.pack()
    btn_close = tk.Button(master=popup, text="close", height= 1, command= popup.destroy) 
    btn_close.pack()
    popup.mainloop()



## __make the objects__

## make the title
txt_title = tk.Label(master=window, 
                    text="pythaoras formula calculator",
                    font=("Arial", 20),)

## make the input fields
txt_a = tk.Label(master=window,text="a = ")
ent_a = tk.Entry(master=window)
txt_b = tk.Label(master=window,text="b = ")
ent_b = tk.Entry(master=window)
txt_c = tk.Label(master=window,text="c = ")
ent_c = tk.Entry(master=window, bg="grey", state="disabled")

## make the buttons
btn_calculate = tk.Button(master=window, text="calculate",bg="green" , height= 3, command=callback_button_calculate)
btn_reset = tk.Button(master=window, text="reset",bg="orange", height= 3, command= callback_button_reset)
btn_quit = tk.Button(master=window, text="quit",  bg="tomato", height= 3, command=window.quit)

## __place the objects__

## place the title
txt_title.grid(row=0, column=0, columnspan=6)

## place the input fields
txt_a.grid(row=1, column=0, sticky=tk.EW)
ent_a.grid(row=1, column=1)
txt_b.grid(row=1, column=2, sticky=tk.EW)
ent_b.grid(row=1, column=3)
txt_c.grid(row=1, column=4, sticky=tk.EW)
ent_c.grid(row=1, column=5)

## place the buttons
btn_calculate.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=tk.EW)
btn_reset.grid(row=2, column=2, columnspan=2, rowspan=2, sticky=tk.EW)
btn_quit.grid(row=2, column=4, columnspan=2, rowspan=2, sticky=tk.EW)



##always at the end
window.mainloop()



