import tkinter as tk 

window=tk.Tk()
window.title("Login")
window.geometry("200x300") 


def callback_button_login():
    print("login")

def callback_button_register():
    print("register")





txt_username = tk.Label(master=window,text="Username: ")
ent_username = tk.Entry(master=window)
txt_password = tk.Label(master=window,text="Password: ")
ent_password = tk.Entry(master=window)

## make the buttons
btn_login = tk.Button(master=window, text="Login", height= 1, command= callback_button_login)
btn_register = tk.Button(master=window, text="Register", height= 1, command= callback_button_register)


## make the layout
txt_username.grid(row=0, column=0)
ent_username.grid(row=0, column=1)
txt_password.grid(row=1, column=0)
ent_password.grid(row=1, column=1)
btn_login.grid(row=2, column=0, sticky= tk.EW)
btn_register.grid(row=2, column=1, sticky= tk.EW)






## at the end
window.mainloop()