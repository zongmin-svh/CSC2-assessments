from tkinter import*

from tkinter import ttk
root = Tk()

# Creating the title
root.title("Julie's Party Hire")

# Creating a frame fro editing
frame = LabelFrame(root, text ='Customers Information', padx=100, pady=20)
frame.pack()

#Creating the labels
n1= Label(frame,text='Full name')
n1.grid(row=0, column=0)

p1 = Label(frame, text="Receipt number")
p1.grid(row=1, column=0)

t1 = Label(frame, text='Item hired')
t1.grid(row=2, column=0)

s1 = Label(frame, text='Number hired')
s1.grid(row=3, column=0)

x1 = Label(frame, text='Date')
x1.grid(row=4, column=0)

# entry boxes
name_box = Entry(frame)
name_box.grid(row=0, column=1)

receipt_box = Entry(frame)
receipt_box.grid(row=1, column=1)

item_box = Entry(frame)
item_box.grid(row=2, column=1)

number_box = Entry(frame)
number_box.grid(row=3, column=1)

date_box = Entry(frame)
date_box.grid(row=4, column=1)



# creating a table frame
my_table = ttk.Treeview(root)

# define the columns
my_table['columns'] = ('Full name', 'Receipt number', 'Item hired', 'Number hired', 'Date')


#Creating the columns
my_table.column("#0", width=1,  stretch=NO)
my_table.column("Full name", anchor=CENTER, width=200)
my_table.column("Receipt number", anchor=CENTER, width=200)
my_table.column("Item hired", anchor=CENTER, width=200)
my_table.column("Number hired", anchor=CENTER, width=200)
my_table.column("Date", anchor=CENTER, width=200)


# Create the heading
my_table.heading("#0", text="", anchor=CENTER)
my_table.heading("Full name", text="Full name", anchor=CENTER)
my_table.heading("Receipt number", text="Receipt number", anchor=CENTER)
my_table.heading("Item hired", text="Item hired", anchor=CENTER)
my_table.heading("Number hired", text="Number hired", anchor=CENTER)
my_table.heading('Date', text='Date', anchor=CENTER)
my_table.pack(pady=30)


# define submit function
def submit():
    my_table.insert(parent='', index='end', values=(name_box.get(), receipt_box.get(), item_box.get(), number_box.get(), date_box.get()))
    # clear the boxes
    name_box.delete(0, END)
    receipt_box.delete(0, END)
    item_box.delete(0, END)
    number_box.delete(0, END)
    date_box.delete(0, END)

# define delete functions
def clear():
    # clear the boxes
    name_box.delete(0, END)
    receipt_box.delete(0, END)
    item_box.delete(0, END)
    number_box.delete(0, END)
    date_box.delete(0, END)

def delete_one():
    x = my_table.selection()[0]
    my_table.delete(x)

# buttons
submit = Button(frame, text='submit', command=submit)
submit.pack()

# delete buttons
clear = Button(frame, text='Clear', command=clear)
clear.pack()



















delete = Button(root, text='Delete selected', command=delete_one)
delete.pack()


root.mainloop()