import json
import tkinter as tk
import os
from pathlib import Path

path = Path.cwd()
print(os.listdir(path))

path = f"{(path)}/Python/flashcard/packs/"
dir = os.listdir(path)


class Flashcard():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x400")
        self.root.title("multipage gui")
        self.root.grid_columnconfigure(3, weight=2)
        self.current_card = 0
        self.listbox_selection = None
        self.current_file = None
        

        self.pages = {"home":         self.home, 
                      "pack_select":  self.pack_select, 
                      "pack_view":    self.pack_view, 
                      "pack_create":  self.pack_create, 
                      "pack_delete":  self.pack_delete, 
                      "pack_edit":    self.pack_edit}
        
        
        self.current_items = []

        print (f"getting packs from:  {path}")
        self.current_page = "home"
        self.change_page("home")

    def destroy(self):
        for i in self.current_items:
            for item in i:
                item.place_forget()
                item.grid_forget()
                item.pack_forget()
        self.current_items = [] 

    def change_page(self, page, commands=None):
        self.destroy()

        if commands != None:
            self.pages[page](commands)
        else:
            self.pages[page]()
        self.current_page = page


    
    def home(self):
        self.title =tk.Label(self.root, text="home page", width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
        self.text  =tk.Label(self.root, text="This is the home page, you can choose to view your flashcard packs or create a new one", width=70, height=3, font=("Helvetica", 10))
        self.current_card = 0
        self.current_file = None

        self.bt_edit_pack     =tk.Button(self.root, text="edit packs",      command=lambda: self.change_page("pack_select","Edit"), width=20)
        self.flashcard_packs  =tk.Button(self.root, text="flashcard packs", command=lambda: self.change_page("pack_select", "View"), width=20)
        self.bt_new_pack      =tk.Button(self.root, text="new pack",        command=lambda: self.change_page("pack_create"),       width=20)


        self.title.grid (row=0, column=0, sticky="nsew")
        self.text.grid  (row=1, column=0, sticky="nsew")

        self.flashcard_packs.grid (row=4, column=0, sticky="nsew")
        self.bt_edit_pack.grid    (row=5, column=0, sticky="nsew")
        self.bt_new_pack.grid     (row=6, column=0, sticky="nsew")

        

        self.current_items.append([self.title, self.text, self.bt_new_pack, self.flashcard_packs, self.bt_edit_pack])
    
    def pack_select(self, select):

        self.title =tk.Label(self.root, text="Pack select", width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
        self.text  =tk.Label(self.root, text="This is the Pack selection, you can Open already created packs here", width=70, height=3, font=("Helvetica", 10))



        self.homebutton = tk.Button(self.root, text="home", command=lambda: self.change_page("home"), width=20)
        self.homebutton.place(y=375)

        self.listbox = tk.Listbox(self.root, height= 10, selectmode="single", width=50)
        self.listbox.grid(column=0,row=2,rowspan=3, sticky="nsew")

        ## iterate through the directory and create a button for each file without the extension.
        for i in dir:
            text = i.split(".")
            self.listbox.insert("end", text[0])

        ## if select is true, then the user is selecting a pack to open, if false, then the user is selecting a pack to edit
        if select == "View":
            self.open_button = tk.Button(self.root, text="open", command=lambda: self.change_page("pack_view", f"{self.listbox.get(tk.ANCHOR)}.json"), width=20)
            self.title =tk.Label(self.root, text="Pack select", width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
            self.text  =tk.Label(self.root, text="This is the Pack selection, you can Open already created packs here", width=70, height=3, font=("Helvetica", 10))
        elif select == "Edit": 
            self.open_button = tk.Button(self.root, text="Edit", command=lambda: self.change_page("pack_edit", f"{self.listbox.get(tk.ANCHOR)}.json"), width=20)
            self.title =tk.Label(self.root, text="Pack edit", width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
            self.text  =tk.Label(self.root, text="This is the Pack edit, you can edit already created packs here", width=70, height=3, font=("Helvetica", 10))
        self.open_button.grid (column=0, row=5, rowspan=2, sticky="nesw")
        self.title.grid       (row=0, column=0, sticky="nsew")
        self.text.grid        (row=1, column=0, sticky="nsew")



        ## add to current items so it can be destroyed
        print("assigning current items")
        self.current_items.append([self.listbox, self.open_button, self.homebutton, self.title, self.text])

    def pack_view(self, filename):
        ## ___get the file content__
        ## if the file is not found, then return to the pack select page
        if filename == ".json":
            print ("file not found")
            self.change_page("pack_select", True)
            return
        ## set the current file to the file name, then use json to convert the file to a library
        self.current_file = filename
        file = open(f"{path}{filename}", "r")
        content = json.loads(file.read())

        ## set the title to the file name
        self.title =tk.Label (self.root, text= filename.split(".")[0] , width=20, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
        self.title.grid      (row=0, column=0, sticky="nsew")
        
        ## get the packs description
        self.text  =tk.Label (self.root, text=content["descripton"], width=70, height=3, font=("Helvetica", 10))
        self.text.grid       (row=1, column=0, sticky="nsew")
        
        self.question_number = tk.Label(self.root, text=f"Question {self.current_card+1} of {len(content['flashcards'])}", width=20, height=2, font=("Helvetica", 10), background="grey")
        self.question_number.place (x=0, y=0)

        ## create the home button
        self.homebutton = tk.Button (self.root, text="home", command=lambda: self.change_page("home"), width=20)
        self.homebutton.place       (y=375)

        ## question box
        self.question_box = tk.Label(self.root, height= 10, width=25, text= content["flashcards"][self.current_card]["question"] )
        self.question_box.place(x=50, y=150)

        ## answer box
        self.answer_box = tk.Text(self.root, height= 10, width=20 )
        self.answer_box.place(x=250, y=150)

        ## submit button
        self.submit_button = tk.Button(self.root, text="submit", command=lambda: self.check_answer(content["flashcards"][self.current_card]["accepted_answers"]), width=22, height=1)
        self.submit_button.place(x=250, y=300)
        
        ## next and previous buttons
        self.next_button = tk.Button(self.root, text="next", command=lambda: self.change_card(True), width=22, height=1)
        self.next_button.place(x=400, y=375)
        self.previous_button = tk.Button(self.root, text="previous", command=lambda: self.change_card(False), width=22, height=1)
        self.previous_button.place(x=250, y=375)

        ## disable and enable the next/prev buttons depending on the position in the pack
        if self.current_card == 0:
            self.previous_button.config(state="disabled")
        if self.current_card == len(content["flashcards"])-1:
            self.next_button.config(state="disabled")

        ## append to current items for removal
        self.current_items.append([self.question_box, self.answer_box, self.homebutton, self.title, self.text, self.submit_button, self.next_button, self.previous_button, self.question_number])

        ## testing 
        #print (content["flashcards"][self.current_card]["question"])
        #print (content["flashcards"][self.current_card]["model_answer"])
        #print (content["flashcards"][self.current_card]["accepted_answers"])

    def change_card(self, next):
        ## change card
        if next:
            self.current_card += 1
        else:
            self.current_card -= 1

        self.change_page("pack_view",self.current_file)

    def check_answer(self, accepted_answers):
        ## get the input from the answer box
        answer = self.answer_box.get("1.0", "end-1c").strip().lower()

        ## check if the answer is in the accepted answers
        if answer in accepted_answers:
            ## set the answer box to green
            self.answer_box.config(background="light green")
        else:
            ## set the answer box to red
            self.answer_box.config(background="pink")


    def pack_create(self):
        print ("pack_create")

    def pack_edit(self, filename):
        if filename == ".json":
            print ("file not found")
            self.change_page("pack_select", True)
            return
        self.current_file = filename
        file = open(f"{path}{filename}", "r")
        content = json.loads(file.read())


        self.homebutton = tk.Button (self.root, text="home", command=lambda: self.change_page("home"), width=20)
        self.homebutton.place       (y=375)

        self.title =tk.Label (self.root, text= filename.split(".")[0] , width=34, height=2, font=("Helvetica", 20), bg="grey", fg="black", )
        self.title.grid      (row=0, column=0, sticky="nsew")


        self.description = tk.Text(self.root, width=34, height=5, font=("Helvetica", 10),bg="light Grey", fg="black")
        self.description.insert("1.0", content["descripton"])
        self.description.grid(row=1, column=0, sticky="nsew")

        self.listbox = tk.Listbox(self.root, width=34, height=10, font=("Helvetica", 10),bg="light Grey", fg="black")
        self.listbox.grid(row=2, column=0, sticky="nsew")
        for i in content["flashcards"]:
            self.listbox.insert("end", f"{i['question']}")

        self.remove_button = tk.Button(self.root, text="Remove Question", command=lambda: self.question_delete(filename, self.listbox.curselection()[0]), width=20)
        self.remove_button.grid(row=3, column=0, sticky="nsew")


        self.current_items.append([self.homebutton, self.description, self.listbox, self.title, self.remove_button])
    
    def question_delete(self, filename, i):
        print("question_delete", filename, i)
        self.change_page("pack_edit", filename)

    def pack_delete(self, filename):
        print("pack_delete", filename)
        



app = Flashcard()
app.root.mainloop()
