import json
import tkinter as tk
import os
from pathlib import Path

path = Path.cwd()
path = f"{(path)}/single file stuffs/flashcard/packs/"
dir = os.listdir(path)
print (dir)


class Flashcard():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x400")
        self.root.title("multipage gui")
        self.root.grid_columnconfigure(3, weight=2)
        

        self.pages = {"home": self.home, "pack_select": self.pack_select, "pack_view": self.pack_view, "pack_create": self.pack_create}
        self.current_items = []


        print (dir)
        print (path)
        self.current_page = "home"
        self.change_page("home")


    def change_page(self, page, commands=None):
        self.destroy()
        if commands != None:
            print(f"page has command, passing {page}, {commands}")
            self.pages[page](commands)
        else:
            print(f"page has no command  {page}, {commands}")
            self.pages[page]()
        self.current_page = page

    def destroy(self):
        for i in self.current_items:
            for button in i:
                button.place_forget()
                button.grid_forget()
        self.current_items = []
    
    def home(self):
        self.title =tk.Label(self.root, text="home page", width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
        self.text = tk.Label(self.root, text="this is the home page, you can choose to view your flashcard packs or create a new one", width=70, height=3, font=("Helvetica", 10))


        self.bt_new_pack =tk.Button(self.root, text="create pack", command=lambda: self.change_page("pack_select"), width=20)
        self.flashcard_packs  =tk.Button(self.root, text="flashcard packs", command=lambda: self.change_page("pack_select"), width=20)


        self.title.grid(row=0, column=0, sticky="nsew")
        self.text.grid (row=1, column=0, sticky="nsew")

        self.bt_new_pack.place(x=350, y=200, anchor="center")
        self.flashcard_packs.place(x=200, y=200, anchor="center")

        self.current_items.append([self.title, self.text, self.bt_new_pack, self.flashcard_packs])
    

    def pack_select(self):

        ## list of buttons, need to figure out how to limit the height and make the scroll bar actually function.
        self.listbox = tk.Listbox(height=4, width=10, background="grey", font=("Helvetica", 10))
        self.listbox.place(x=100, y=200, anchor="center")

        self.scrollbar = tk.Scrollbar(self.listbox, orient="vertical")
        self.scrollbar.pack(side="right", fill="both")

        self.scrollbar.config(command=self.listbox.yview)
        self.current_items.append([self.listbox, self.scrollbar])

        ## iterate through the directory and create a button for each file without the extension.
        for i in dir:
            text = i.split(".")
            self.pack_link = tk.Button(self.listbox, text=text[0], command=lambda file_name=i: self.change_page("pack_view", file_name), width=20)
            self.listbox.insert(1,self.pack_link.pack())


    def pack_view(self, file_name):

        ## read file
        print(f"pack_view:  {file_name}")
        file = open(f"{path}{file_name}", "r")
        content = json.loads(file.read())
        print (content["descripton"])
        print (content["flashcards"][0]["question"])
        print (content["flashcards"][0]["answer"])
        
        
    
    def pack_create(self):
        print ("pack_create")



app = Flashcard()
app.root.mainloop()
