# impprt the tkinter to this project
from tkinter import*
import tkinter as tk
from tkinter import ttk

# massagebox allows the popup messages
from tkinter import messagebox

# Calendar function involved
from tkcalendar import*


# put everything into the root
root = Tk()

# Creating the title of this project
root.title("Julie's Party Hire")


# adding the instuctions
instruction = Label(root, text="!!!! Instructions !!!!: Enter the correct information to the entry-boxes. Click submit button to insert the info to the table.")
instruction.pack(pady=20)

# Creating a frame for information editing
frame = LabelFrame(root, text ='Customers Information', padx=100, pady=20)
frame.pack()



# Labels for the entry boxes within the frame
n1= Label(frame,text='Full name')
n1.grid(row=0, column=0) # using grid() to put everything in order

p1 = Label(frame, text="Receipt number")
p1.grid(row=1, column=0)

t1 = Label(frame, text='Item hired')
t1.grid(row=2, column=0)

s1 = Label(frame, text='Number hired')
s1.grid(row=3, column=0)

x1 = Label(frame, text='Date')
x1.grid(row=4, column=0)


# Stringvar helps to manages the varables within a widget
my_w= tk.StringVar(root)


# The entry boxes to collect the information, also located in the frame created
name_box = Entry(frame)
name_box.grid(row=0, column=1)

receipt_box =Entry(frame)
receipt_box.grid(row=1, column=1)

item_box = Entry(frame)
item_box.grid(row=2, column=1)

number_box = Entry(frame)
number_box.grid(row=3, column=1)

# define a function that allows to create a calendar for date selecting
def pick_date(event):
    global frame, cal,but
    cal = Calendar(frame, selectmode='day', year=2023, month=5, day=22)
    cal.grid(row=5, column=1)
    
    # button to confirm the date selected
    but= Button(frame, text='confirm', command=grab_date)   
    but.grid(row=6, column=1)

def grab_date(): 
    date_box.delete(0, END)
    date_box.insert(0, cal.get_date()) # insert the date picked from the calnedar into the date_box
    cal.destroy()
    but.destroy()
# create a date entry box   
date_box = Entry(frame, textvariable=my_w)
date_box.grid(row=4, column=1)
date_box.bind('<1>', pick_date)
# calendar popup as soon as the date_box is clicked






# define submit function, plus the problem checker for the information filled in before submit to the treeview.
def submit():
    receipt=receipt_box.get()
    name=name_box.get()
    item=item_box.get()
    number=number_box.get()
    # conditons listed
    if len(name_box.get())==0 and len(receipt_box.get())==0 and len(item_box.get())==0 and len(number_box.get())==0 and len(date_box.get())==0:  
        msg = 'Please fill in valid info'
        messagebox.showerror('error',msg)
        # if all the entry boxes are empty, pop up an errro message.
        
    elif len(name_box.get())<5 or any(ch.isdigit() for ch in name):
        msg='Enter your valid full name please'
        messagebox.showerror('error',msg)
        # if there are numbers in name or less alpha means it's not a full name, pop up an error message
        
    elif len(receipt_box.get()) ==0 or any(ch.isalpha() for ch in receipt):
        msg='Enter the valid receipt number please'
        messagebox.showerror('error',msg)
        # if receipt number entered involved a alpha, or it's empty, pop up an error message
        
    elif len(item_box.get())==0 or any(ch.isdigit() for ch in item):
           msg='Enter the valid item please'
           messagebox.showerror('error',msg)
           # if item_box is empty or if item invloved any numbers, pop up an error message
           
    elif any(ch.isalpha() for ch in number) or len(number_box.get())==0:
           msg='Enter valid number of item please(1-500)'
           messagebox.showerror('error',msg)
           # if number_box is not number or if it is not between 1-500, or if it's empty, pop up an error message
           
    elif len(date_box.get())==0 or any(ch.isalpha() for ch in date_box.get()):
           msg='Enter the valid date please'
           messagebox.showerror('error',msg)  
           # if the date_box is empty, pop up an error message
    else:
        # define the submit function that transfer the data from the entry boxes to the treeview table
        my_table.insert(parent='', index='end', values=(name_box.get(), receipt_box.get(), item_box.get(), number_box.get(), date_box.get()))
        # clear the boxes once the date has been submitted
        name_box.delete(0, END)
        receipt_box.delete(0, END)
        item_box.delete(0, END)
        number_box.delete(0, END)
        date_box.delete(0, END)  






# define delete functions
def clear():
    # clear the the information from the entry boxes
    name_box.delete(0, END)
    receipt_box.delete(0, END)
    item_box.delete(0, END)
    number_box.delete(0, END)
    date_box.delete(0, END)
    cal.destroy()

# buttons
button1 = Button(frame, text = 'Submit',command=submit) # submit the data
button1.grid(row=1, column=2)

button2 = Button(frame, text='clear', command=clear) # delete the data
button2.grid(row=3, column=2)





# add some style to the treeview table
style = ttk.Style()
# pick a theme
style.theme_use('clam')
# configure the color from treeview
style.configure("Treeview",
                background='silver',
                foreground='black',
                rowheight=25,
                fieldbackground='silver')

# change the selected color
style.map("Treeview",
          background=[('selected','green')])








# create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# treeview scrollbar if needed
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# creating a table frame
my_table = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
tree_scroll.config(command=my_table.yview)







# define the columns from the table
my_table['columns'] = ('Full name', 'Receipt number', 'Item hired', 'Number hired', 'Date')

#Creating the columns
my_table.column("#0", width=1,  stretch=NO)
my_table.column("Full name", anchor=CENTER, width=200)
my_table.column("Receipt number", anchor=CENTER, width=200)
my_table.column("Item hired", anchor=CENTER, width=200)
my_table.column("Number hired", anchor=CENTER, width=200)
my_table.column("Date", anchor=CENTER, width=200)


# Create the heading fro the columns
my_table.heading("#0", text="", anchor=CENTER)
my_table.heading("Full name", text="Full name", anchor=CENTER)
my_table.heading("Receipt number", text="Receipt number", anchor=CENTER)
my_table.heading("Item hired", text="Item hired", anchor=CENTER)
my_table.heading("Number hired", text="Number hired", anchor=CENTER)
my_table.heading('Date', text='Date', anchor=CENTER)
my_table.pack(pady=20)





# define the function for deleting the data from the treeview table
def delete_one():
    x = my_table.selection()[0]
    my_table.delete(x)
# delete button
delete = Button(root, text='Delete selected', command=delete_one)
delete.pack(pady=5)








# call the mainloop to be able to run it.
root.mainloop()



