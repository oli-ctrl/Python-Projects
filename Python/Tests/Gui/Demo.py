import tkinter as tk

class app():
    def __init__(self):
        ## create the window
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Test Gui")

        self.current_page = "home"
        ## dict of pages linking to the page functions, allows to call the page by name 
        self.pages = {"home": self.Home(self.root, self), "page1": self.Page1(self.root, self), "page2": self.Page2(self.root, self)}
        self.current_items = []

        ## start the gui on the home page
        self.change_page("home")

    ## change the page
    def change_page(self, page):
        ## hide the current page
        self.pages[self.current_page].hide()
        ## call the page function
        self.pages[page].show()
        self.current_page = page

    ## destroy all the items on the page

    ## parent page class
    class Page:
        ## saves some params for every page
        def __init__(self, root, manager):
            self.manager = manager
            self.root = root
            self.items = []
            self.positions = []
            
        ## shows all the items on the page
        def show(self):
            for item in self.items:
                item.place(self.positions[self.items.index(item)])
            pass

        ## saves the position of all the items on the page
        def getpos(self):
            for item in self.items:
                self.positions.append(dict(item.place_info()))

        ## hides all the items on the page
        def hide(self):
            ## if the positions are not saved, save them
            if len(self.positions) == 0:
                self.getpos()
            ## hide all the items on the page
            for item in self.items:
                item.place_forget()

    ## child page classes
    class Home(Page):
        def __init__(self, root, manager):
            super().__init__(root, manager)

            ## create the items on the page
            self.title =tk.Label(self.root, text="home page")
            self.bt_home =tk.Button(self.root, text="home", command=lambda: manager.change_page("home"))
            self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: manager.change_page("page1"))
            self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: manager.change_page("page2"))

            ## place the items on the page
            self.title.place(x=0, y=0)
            self.bt_home.place(x=0, y=40)
            self.pg_1.place(x=60, y=40)
            self.pg_2.place(x=120, y=40)

            ## save the items in a list and hide
            self.items = self.title,self.bt_home,self.pg_1,self.pg_2
            self.hide()


    class Page1(Page):
        def __init__(self, root, manager):
            super().__init__(root, manager)
            self.title =tk.Label(self.root, text="page 1")
            self.bt_home =tk.Button(self.root, text="home", command=lambda: manager.change_page("home"))
            self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: manager.change_page("page1"))
            self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: manager.change_page("page2"))
            self.title.place(x=0, y=0)
            self.bt_home.place(x=0, y=40)
            self.pg_1.place(x=60, y=40)
            self.pg_2.place(x=120, y=40)
            self.items = self.title,self.bt_home,self.pg_1,self.pg_2
            self.hide()

    class Page2(Page):
        def __init__(self, root, manager):
            super().__init__(root, manager)
            self.title =tk.Label(self.root, text="page 2")
            self.bt_home =tk.Button(self.root, text="home", command=lambda: manager.change_page("home"))
            self.pg_1  =tk.Button(self.root, text="page 1", command=lambda: manager.change_page("page1"))
            self.pg_2  =tk.Button(self.root, text="page 2", command=lambda: manager.change_page("page2"))
            self.title.place(x=0, y=0)
            self.bt_home.place(x=0, y=40)
            self.pg_1.place(x=60, y=40)
            self.pg_2.place(x=120, y=40)
            self.items = self.title,self.bt_home,self.pg_1,self.pg_2
            self.hide()


## run the app
test=app()
test.root.mainloop()