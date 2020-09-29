from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Creating Radio Buttons")
root.geometry("455x452")
root.minsize(200,300)
root.maxsize(500,520)


def order():
    tmsg.showinfo("Your order", f"You ordered {variablee.get()}")


variablee = StringVar()
#variablee.set("Radio")      #Agar koi initial value nhi deta like mne yaha "Radio" dia h to sab ke sab select ho jate. Initial value dene se sab options initially unselected rehte h. Jarroori nhi h ki main "Radio" hi likhu m kuch aur bhi likh sakta hu jaise "jugnu", "a", "cddgd", etc
variablee.set("Dosa")       #"set" karne se vhi initially select hoga jo ape likha h

Label(root, text="What would you like to eat Sir!", font="verdana 19 italic").pack(pady=14)
radio = Radiobutton(root, text="Dosa", padx=12, variable=variablee, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idli", padx=12, variable=variablee, value="Idli").pack(anchor="w")
radio = Radiobutton(root, text="Sambhar Vada", padx=12, variable=variablee, value="Sambhar Vada").pack(anchor="w")
radio = Radiobutton(root, text="Noodles", padx=12, variable=variablee, value="Noodles").pack(anchor="w")

Button(root, text="Submit", bg="lightgreen", fg="blue", command=order).pack()






#Listbox

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")  #"ACTIVE" matlab jo bhi menu mne select kar rakhi h usse pehle add ho jaega

    i+=1
    
i=0

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First element of the box")     #"END" matlab jo bhi likha h uske baad m add kare, initially kuch nhi likha hota so initially "END" starting m add kar deta h
lbx.insert(END, "Second element of the box")
lbx.insert(END, "Third element of the box")
lbx.insert(END, "Fourth element of the box")


Button(root, text="Add Item", command=add).pack()


root.mainloop()