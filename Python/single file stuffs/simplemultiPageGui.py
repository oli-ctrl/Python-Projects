import tkinter as tk

class app():
    def __init__(self):
        ## create the window
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("multipage gui")

        self.current_page = "home"

        ## dict of pages linking to the page functions
        self.pages = {"home": self.home, "page1": self.page1, "page2": self.page2}
        self.current_items = []


        self.change_page("home")

    def change_page(self, page):
        self.destroy()
        self.pages[page]()
        self.current_page = page


    def destroy(self):
        for i in self.current_items:
            for button in i:
                button.place_forget()
        self.current_items = []

    def home(self):
        self.title =tk.Label(self.root, text="home page")
        self.bt_home =tk.Button(self.root, text="home", command=lambda: self.change_page("home"))
        self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: self.change_page("page1"))
        self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: self.change_page("page2"))
        self.title.place(x=0, y=0)
        self.bt_home.place(x=0, y=40)
        self.pg_1.place(x=60, y=40)
        self.pg_2.place(x=120, y=40)
        self.current_items.append([self.title,self.bt_home,self.pg_1,self.pg_2])


    def page1(self):
        self.title =tk.Label(self.root, text="page 1")
        self.bt_home =tk.Button(self.root, text="home", command=lambda: self.change_page("home"))
        self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: self.change_page("page1"))
        self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: self.change_page("page2"))
        self.title.place(x=0, y=0)
        self.bt_home.place(x=0, y=40)
        self.pg_1.place(x=60, y=40)
        self.pg_2.place(x=120, y=40)
        self.current_items.append([self.title,self.bt_home,self.pg_1,self.pg_2])

    def page2(self):
        self.title =tk.Label(self.root, text="page 2")
        self.bt_home =tk.Button(self.root, text="home", command=lambda: self.change_page("home"))
        self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: self.change_page("page1"))
        self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: self.change_page("page2"))
        self.title.place(x=0, y=0)
        self.bt_home.place(x=0, y=40)
        self.pg_1.place(x=60, y=40)
        self.pg_2.place(x=120, y=40)
        self.current_items.append([self.title,self.bt_home,self.pg_1,self.pg_2])

test=app()

test.root.mainloop()