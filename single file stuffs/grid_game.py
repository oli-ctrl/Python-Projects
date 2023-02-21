import tkinter as tk
import random

## change these to change the window size.
width = 5
height = 4


## random global variables
count = 0
allbuttons = []
status = "None"
normalposprev = "None"
normalpos = "None"
reset_count = 0 

## list of every possible button, change this to change the amount of buttons, or the text on the buttons
baselist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



## check if the width and height are valid for the length of the base list given
def check_valid(width,height,baselist):
    ## make sure the size of the grid is not bigger than the length of the list * 2 (*2 because each button has a pair)
    multiplied = width * height
    if multiplied > len(baselist)*2:
        return False
    ## check if the multiplied number is even
    check = multiplied % 2
    if check == 0:
        return True
    else:
        return False

## generate list of 2x each item
def generate_list(baselist): 
    list = []
    amount = (width * height)/2
    ## interate through the list twice for the lenght of the amount of buttons needed
    for i in range(0,2):
        for i in range(0,int(amount)):
            list.append(baselist[i])
    ## shuffle the list
    random.shuffle(list)
    return list

# button callback
def callback_button(position):
    global normalpos
    global status
    global reset_count
    

    ## only run if the game isnt resetting
    if status != "reset":
        ## get normal position (0-...) then set normalpos to this
        normalposlist = str(position).split("n")
        if normalposlist[1] == "":
            normalposlist[1] = 1
        normalpos = int(normalposlist[1])-1

        ## set the text of the button to its position in the list, then set the game status to check
        allbuttons[normalpos].config(text=Lists[normalpos])
        status = "check"

## used by make window to shuffle the base list
def shuffle():
    global baselist
    random.shuffle(baselist)

## make window and lists
def make_window():
    global count 
    global Lists
    global width
    global height
    global allbuttons
    global Lists
    Lists = []
    allbuttons = []
    count = 0 
    ## shuffle the base list so later elements have a chance of showing up commonly, then generate the list
    shuffle()
    Lists = generate_list(baselist)

    ## check if the width and height specified are valid.
    if check_valid(width,height,baselist) == False:
        ## set the window text to invalid width and height and populate it with reset button
        text = tk.Label(master=window, text="invalid width and height")
        text.grid(row=0, column=0)
        button = tk.Button (master=window, text="close", command=window.destroy)
        button.grid (row=1, column=0)
        return
    else:
        ## make the window the correct size for the width and height specified
        window.geometry("{}x{}".format((width*100), (height*100)))
        for i in range(width):
            for j in range(height):
                ## make the button and add it to the grid aswell as giving it a command to run when clicked, and a position for future checks.
                btn = tk.Button(master=window,state="active" , text="?", height= 6, width=13, bg="white" ,fg="black", command=lambda i=count: callback_button(allbuttons[i]))
                btn.grid(row=j, column=i, sticky= tk.EW)
                count += 1
                ## add the button to a list of all buttons, this is so that it can be checked and change later using the position
                allbuttons.append(btn)
        window.after(1000, main_loop)
        window.mainloop()

## mainloop
def main_loop():
    global status
    global normalposprev
    global normalpos
    global reset_count
    
    ## used for debugging
    #print (f"main loop: status: {status} normalpos: {normalpos} normalposprev: {normalposprev}" )

    if status == "reset":   ## reset all enabled buttons to "?"
        ## iterate the reset count till it reaches 500 then reset the game 
        reset_count += 1
        if reset_count > 500:
            reset_count = 0
            status = "None"
            ## run over every button, check if its enabled, if it is then set the text to "?"
            for i in range(0,len(allbuttons)):
                if allbuttons[i].cget("state") == "normal":
                        allbuttons[i].config(text="?")
       

    elif status == "check": ## if the status is check, do stuff to see if it is a match
        try:
            ## check if the button clicked is the same as the previous button clicked, if it is then set the status to reset
            if normalposprev == normalpos:
                status = "reset"

            ## check if the text on the button pushed is the same as the text of the previous button. if it is then disable the button and make it green
            elif Lists[normalpos] == Lists[normalposprev]:
                allbuttons[normalpos].config(state="disabled", bg="lightgreen", fg="red")
                allbuttons[normalposprev].config(state="disabled",bg="Lightgreen", fg="red")
                status = "none"
    
            ## reset the normalpositions.
            normalpos = "None"
            normalposprev = "None"
        
        ## this sometimes get called when it tries to use the above function with a normalpos or normal pos prev of none.
        except:
            status = "none"
            normalposprev = normalpos

    ## re-add the function to main loop. 
    window.after(1, main_loop)

## make window and give it tittle
window=tk.Tk()
window.title("grid game (REAL)")
## calls the make window function
make_window()

window.mainloop()
