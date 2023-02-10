import tkinter as tk
import random 


count = 0
width = 2
height = 2
allbuttons = []
turn = "None"
normalsposlast = "None"



def check_valid(width,height):
    multiplied = width * height
    if multiplied > 52:
        return False
    check = multiplied % 2
    if check == 0:
        return True
    else:
        return False

def generate_list():
    baselist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list = []
    amount = (width * height)/2
    for i in range(0,2):
        for i in range(0,int(amount)):
            list.append(baselist[i])
    random.shuffle(list)
    return list

def callback_button(position):
    global turn
    global normalposprev

    ## get normal position
    normalposlist = str(position).split("n")
    if normalposlist[1] == "":
        normalposlist[1] = 1
    normalpos = int(normalposlist[1])-1

    ## set button text to list
    allbuttons[normalpos].config(text=Lists[normalpos])

    ## check if first button
    if turn == "None":
        turn = normalpos
        normalposprev = normalpos
        


    ## check if same button
    elif turn != "None":
        if normalposprev == normalpos:
            print("same button")

        ## check correct 
        elif Lists[turn] == Lists[normalpos]:
            print("correct")
            allbuttons[normalpos].config(state="disabled", bg="lightgreen", fg="red")
            allbuttons[turn].config(state="disabled",bg="Lightgreen", fg="red")
            turn = "None"
            normalposprev = "None"
            return
        else:
            print("incorrect")
        
         ## reset turn
        normalposprev = normalpos
        turn = "None"
        for i in range(0,len(allbuttons)):
            if allbuttons[i].cget("state") == "normal":
                allbuttons[i].config(text="?")



        
if check_valid(width,height) == False:
    print("invalid width and height")
    exit()

Lists = generate_list()



window=tk.Tk()
window.title("grid game")
window.geometry("{}x{}".format((width*100), (height*100)))
window.config(bg="white")

for i in range(0,width):
    for j in range(0,height):
        btn = tk.Button(master=window,state="active" , text="?", height= 6, width=13, bg="white" ,fg="black", command=lambda i=count: callback_button(allbuttons[i]))
        btn.grid(row=j, column=i, sticky= tk.EW)
        count += 1
        allbuttons.append(btn)
        

window.mainloop()

