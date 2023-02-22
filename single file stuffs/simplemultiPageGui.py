import tkinter as tk

class app():
    def __init__(self):
        ## create the window
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("multipage gui")

        self.current_page = "home"
        self.pages = {"home": self.home, "page1": self.page1, "page2": self.page2}


        self.change_page("home")

    def change_page(self, page):
        self.pages[self.current_page]("yes")
        self.pages[page]()
        self.current_page = page
        

    def home(self, destroy="no"):
        if destroy != "yes":
            self.title =tk.Label(self.root, text="home page")
            self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: self.change_page("page1"))
            self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: self.change_page("page2"))
            self.title.place(x=0, y=0)
            self.pg_1.place(x=0, y=20)
            self.pg_2.place(x=0, y=40)
            return
        try:
            print("destroying")
            self.title.place_forget()
            self.pg_1.place_forget()
            self.pg_2.place_forget()
        except:
            print ("ui does not exist")

    def page1(self, destroy="no"):
        if destroy != "yes":
            self.title =tk.Label(self.root, text="page 1")
            self.pg_1  =tk.Button(self.root, text="home", command=lambda: self.change_page("home"))
            self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: self.change_page("page2"))
            self.title.place(x=0, y=0)
            self.pg_1.place(x=0, y=20)
            self.pg_2.place(x=0, y=40)
            return        
        try:
            print("destroying")
            self.title.place_forget()
            self.pg_1.place_forget()
            self.pg_2.place_forget()
        except:
            print ("ui does not exist")

    def page2(self, destroy="no"):
        if destroy != "yes":
            self.title =tk.Label(self.root, text="page 2")
            self.pg_1  =tk.Button(self.root, text="home", command=lambda: self.change_page("home"))
            self.pg_2  =tk.Button(self.root, text="page 1", command=lambda: self.change_page("page1"))
            self.title.place(x=0, y=0)
            self.pg_1.place(x=0, y=20)
            self.pg_2.place(x=0, y=40)
            return
        try:
            print("destroying")
            self.title.place_forget()
            self.pg_1.place_forget()
            self.pg_2.place_forget()
        except:
            print ("ui does not exist")
    

test=app()

test.root.mainloop()