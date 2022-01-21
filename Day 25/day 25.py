import tkinter
from tkinter.ttk import Label

window = tkinter.Tk()
window.minsize(height=200,width=220)
window.title("Centimeter To Feet Converter")
window.config(padx=200,pady=200)

def button_clicked():
    height=float(entry.get())
    feet=round(height/40.48,2)
    converted_value.config(text=feet)

entry = tkinter.Entry(width=10)
entry.grid(column=1,row=0)

Label(text="Cm").grid(column=2,row=0)
Label(text="is equal to ").grid(column=0,row=1)
converted_value = Label(text="0")
converted_value.grid(row=1,column=1)

Label(text="Feet").grid(column=2,row=1)

tkinter.Button(text="Calculate",command=button_clicked).grid(row=2,column=1)




window.mainloop()