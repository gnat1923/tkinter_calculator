from tkinter import *

root = Tk() # this is the "root" window

'''
#create label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Chris Kenny")

#place widget onto screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
'''
#input data with entry widget (input)
e = Entry(root, width="50", borderwidth="3")
e.pack()
#give field a default value
e.insert(0, "Enter Your Name: ")

#write a function to define what the button does
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#create a button, tie the command (function) to the button
myButton = Button(root,text="Enter Your Name", command=myClick)

#place the button
myButton.pack()

#create "event loop" to keep program running
root.mainloop()
