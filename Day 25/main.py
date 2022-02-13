# import tkinter

  
# def button_clicked():
#     my_label.config(text=input.get())

# window = tkinter.Tk()
# window.title("Hello There")
# window.minsize(width=500,height=300)

# # Label
# my_label= tkinter.Label(text="Let's Try",font=('Arial',22, "bold"))
# button= tkinter.Button(text="Click Me",command=button_clicked)
# input=tkinter.Entry(width=20)
# print(input.get())

# my_label.pack()
# button.pack()
# input.pack()

# window.mainloop()



from tkinter import *
import tkinter
window = tkinter.Tk()
window.title("Grid Testin")
window.minsize(height=400,width=500)
window.config(padx=20,pady=20)


my_label = Label(text="Label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

new_button=Button(text="New Button")
new_button.grid(column=2,row=0)

button= Button(text='Button')
button.grid(column=1,row=1)

entry= Entry(width=32)
entry.grid(column=2,row=3)




window.mainloop()