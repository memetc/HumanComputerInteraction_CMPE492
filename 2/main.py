import os
import sys
from tkinter import *
from tkinter import ttk

py=sys.executable
total = 0

root = Tk()
root.title('Mağaza')
root.geometry("800x800")

# Add some style
style = ttk.Style()
#Pick a theme
style.theme_use("default")
# Configure our treeview colors

style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"
                )
# Change selected color
style.map('Treeview',
          background=[('selected', 'blue')])

# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Ürün", "Kategori", "Fiyat")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Ürün", anchor=W, width=140)
my_tree.column("Kategori", anchor=CENTER, width=100)
my_tree.column("Fiyat", anchor=W, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Ürün", text="Ürün", anchor=W)
my_tree.heading("Kategori", text="Kategori", anchor=CENTER)
my_tree.heading("Fiyat", text="Fiyat", anchor=W)

# Add Data
data = [
    ["Ülker Çikolata (300g)", "Gıda", 22],
    ["Sütaş Süt", "Gıda", 8],
    ["Iphone Sarj Aleti", "Elektronik", 250],
    ["Ikea Yastık", "Ev", 40],
    ["Kola (1lt)", "Gıda", 5],
    ["Kıyma (500g)", "Gıda", 23],
    ["Sandisk USB", "Elektronik", 33],
    ["Somun Füme (100g)", "Gıda", 40],
    ["Tursu (700g)", "Gıda", 10],
    ["Soğan (1kg)", "Gıda", 5],
]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count=0



# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
cart = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
cart.pack()

#Configure the scrollbar
tree_scroll.config(command=cart.yview)

# Define Our Columns
cart['columns'] = ("Ürün", "Kategori", "Fiyat", "Miktar", "Toplam Fiyat")

# Formate Our Columns
cart.column("#0", width=0, stretch=NO)
cart.column("Ürün", anchor=W, width=140)
cart.column("Kategori", anchor=CENTER, width=100)
cart.column("Fiyat", anchor=W, width=80)
cart.column("Miktar", anchor=W, width=80)
cart.column("Toplam Fiyat", anchor=W, width=80)


# Create Headings
cart.heading("#0", text="", anchor=W)
cart.heading("Ürün", text="Ürün", anchor=W)
cart.heading("Kategori", text="Kategori", anchor=CENTER)
cart.heading("Fiyat", text="Fiyat", anchor=W)
cart.heading("Miktar", text="Miktar",anchor=W)
cart.heading("Toplam Fiyat", text="Toplam Fiyat", anchor=W)



for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

    count += 1




add_frame = Frame(root)
add_frame.pack(pady=10)

#Labels
nl = Label(add_frame, text="Ürün")
nl.grid(row=0, column=0)

il = Label(add_frame, text="Kategori")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Fiyat")
tl.grid(row=0, column=2)

tl = Label(add_frame, text="Miktar")
tl.grid(row=0, column=3)




#Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

quantity_box = Spinbox(add_frame, from_=1, to=50)
quantity_box.grid(row=1, column=3)



# Add Record
def add_record():
    f = open("data.txt", "w")

    global total
    total += int(topping_box.get())*int(quantity_box.get())
    f.write(str(total))
    f.close()

    cart.tag_configure('oddrow', background="white")
    cart.tag_configure('evenrow', background="lightblue")
    global count
    if count % 2 == 0:
        cart.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get(), quantity_box.get(), int(topping_box.get())*int(quantity_box.get())), tags=('evenrow',))
    else:
        cart.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get(), quantity_box.get(), int(topping_box.get())*int(quantity_box.get())), tags=('oddrow',))

    count += 1
    # Clear the boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)
    quantity_box.delete(0, END)





# Select Record
def clicker(e):
    # Clear entry boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    # Grab record number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    #temp_label.config(text=values[0])

    # output to entry boxes
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


def checkout():
    os.system('%s %s' % (py, 'checkout.py'))

add_record = Button(root, text="Sepete Ekle", command=add_record)
add_record.pack(pady=10)
add_record = Button(root, text="Satın Al", command=checkout)
add_record.pack(pady=10)


my_tree.bind("<ButtonRelease-1>", clicker)


root.mainloop()