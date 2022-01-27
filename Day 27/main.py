import random
from textwrap import indent
import tkinter
from tkinter.ttk import Entry, Label
from tkinter import messagebox
from turtle import width
from typing import TYPE_CHECKING
import pyperclip
import json
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
    website = website_entry.get().lower()
    email_username = email_username_entry.get()
    password = password_entry.get()

    password_dict = {
        website:{
            "email":email_username,
            "password":password
        }
    }
    ####################### Reading Updating and Dumping JSON Data ########################
    if len(website) !=0 and len(email_username)!=0 and len(password)!=0 :
        is_ok = messagebox.askokcancel(title=website,message=f"Is this correct \n\nEmail : {email_username}\nPassword : {password}")
        if is_ok:
            try:
                with open("Day 27/data.json",'r') as data_file:
                    data = json.load(data_file)
                    data.update(password_dict)

                with open("Day 27/data.json",'w') as data_file:
                    json.dump(data,data_file,indent = 4)
            except FileNotFoundError as exception_message:
                print(f"File not found : {exception_message}")
                with open("Day 27/data.json",'w') as data_file:
                    json.dump(password_dict,data_file, indent=4)
    ########################################################################################

        website_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)
    else:
        messagebox.showerror(title="Error",message = "Please don't leave any fields empty.")

def search_button_clicked():
    try:
        if len(website_entry.get())!=0:
            with open("Day 27/data.json",'r') as data_file:
                data = json.load(data_file)
                password = data[website_entry.get().lower()]["password"]
                email = data[website_entry.get().lower()]["email"]

                messagebox.showinfo(title=website_entry.get().upper(),message= f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showerror(title="Whoops ",message= "Please enter website name in the box first.")

    except FileNotFoundError:
        messagebox.showerror(title="Error",message= "Data file not found. Please add some data first.")
    except KeyError:
        messagebox.showerror(title="Whoops",message = "Website record not found in the database")
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=30,pady=30)
# window.minsize(height=500,width=500)
window.title("Password Manager")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image_location = tkinter.PhotoImage(file="Day 27/logo.png")
canvas.create_image(100 ,100,image=image_location)


# Entrys #
website_entry = Entry(width = 36)
email_username_entry  = Entry(width=62)
password_entry = Entry(width=36)

# Labels #
website = Label(text="Website: ",font=("Arial",10,'bold'))
email_username=Label(text="Email/Username: ",font=("Arial",10,'bold'))
password = Label(text="Password",font=("Arial",10,'bold'))

# Buttons #
generate_password = tkinter.Button(text='Generate Password',width= 21,command=generate_password)
add_button = tkinter.Button(text="ADD",width=36,command=add_button_clicked)
search_button = tkinter.Button(text="Search",width=21,command=search_button_clicked)


# Aligning Buttons #

generate_password.grid(row=3,column=2)
add_button.grid(row=4,column=1,pady=10)
search_button.grid(row=1,column=2)

# Aligning Entries #

website_entry.grid(row=1,column=1)
website_entry.focus()
email_username_entry.grid(row=2,column=1,columnspan=2,pady=5)
email_username_entry.insert(0, "sangamsharma600@gmail.com")
password_entry.grid(row=3,column=1)

# Aligning Labels #
canvas.grid(row=0, column=1) 
website.grid(row=1,column=0)
email_username.grid(row=2,column=0)
password.grid(row=3,column=0)
window.mainloop()