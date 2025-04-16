import tkinter as tk
from tkinter import messagebox as msgbox

#Handling button click event
def button_click():
    #print("Button clicked!")

    #Show an information message box
    msgbox.showinfo("Info", "Welcome to cos102 GUI App!\n")

    #ask for user confirmation
    result=  msgbox.askyesno("Confirmation", "DO you want to continue?")

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#Add a label a widget
label = tk.Label(root, text= "Hello Friend \n ")
label.pack()

#Add a button wodget
button = tk.Button(root, text = "CLick me!", command=button_click)
button.pack()

#Styling the buttton widget
button.config(fg="red", bg="yellow")

#Start the event looop
root.mainloop()

