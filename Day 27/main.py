import random
import tkinter
from tkinter.ttk import Entry, Label
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_numbers+password_symbols+password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.delete(0,tkinter.END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
 
def add_button_clicked():
    if len(website_entry.get()) !=0 and len(email_username_entry.get())!=0 and len(password_entry.get())!=0 :
        is_ok = messagebox.askokcancel(title=website_entry.get(),message=f"Is this correct \n\nEmail : {email_username_entry.get()}\nPassword : {password_entry.get()}")
    else:
        messagebox.showerror(title="Error",message = "Please don't leave any fields empty.")

    if is_ok:
        with open("Day 27/data.txt",mode='a') as data:
            data.write(f"|| {website_entry.get()} || {email_username_entry.get()} || {password_entry.get()} || \n")
        website_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)
    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=30,pady=30)
# window.minsize(height=500,width=500)
window.title("Password Manager")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image_location = tkinter.PhotoImage(file="Day 27/logo.png")
canvas.create_image(100 ,100,image=image_location)


# Entrys #
website_entry = Entry(width=35)
email_username_entry  = Entry(width=35)
password_entry = Entry(width=21)

# Labels #
website = Label(text="Website: ",font=("Arial",10,'bold'))
email_username=Label(text="Email/Username: ",font=("Arial",10,'bold'))
password = Label(text="Password",font=("Arial",10,'bold'))

# Buttons #
generate_password = tkinter.Button(text='Generate Password',command=generate_password)
add_button = tkinter.Button(text="ADD",width=36,command=add_button_clicked)


# Aligning Buttons #

generate_password.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)

# Aligning Entries #

website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_username_entry.grid(row=2,column=1,columnspan=2)
email_username_entry.insert(0, "sangamsharma600@gmail.com")
password_entry.grid(row=3,column=1)

# Aligning Labels #
canvas.grid(row=0, column=1) 
website.grid(row=1,column=0)
email_username.grid(row=2,column=0)
password.grid(row=3,column=0)
window.mainloop()