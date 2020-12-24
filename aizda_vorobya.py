import tkinter as tk
from tkinter import ttk

note_bind = 0

root = tk.Tk()

note = ttk.Notebook(root)

frame = tk.Frame(root)
tree1 = ttk.Treeview(frame)
tree1["columns"]=("one","two","three")
tree1.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree1.column("one", width=150, minwidth=150, stretch=tk.NO)
tree1.column("two", width=400, minwidth=200)
tree1.column("three", width=80, minwidth=50, stretch=tk.NO)
tree1.heading("#0",text="Name",anchor=tk.W)
tree1.heading("one", text="Date modified",anchor=tk.W)
tree1.heading("two", text="Type",anchor=tk.W)
tree1.heading("three", text="Size",anchor=tk.W)
tree1.pack()

frame2 = tk.Frame(root)
tree2 = ttk.Treeview(frame2)
tree2["columns"]=("one","two","three")
tree2.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree2.column("one", width=150, minwidth=150, stretch=tk.NO)
tree2.column("two", width=400, minwidth=200)
tree2.column("three", width=80, minwidth=50, stretch=tk.NO)
tree2.heading("#0",text="Name",anchor=tk.W)
tree2.heading("one", text="Date modified",anchor=tk.W)
tree2.heading("two", text="Type",anchor=tk.W)
tree2.heading("three", text="Size",anchor=tk.W)
tree2.pack()

note.add(frame, text="page1")
note.add(frame2, text="page2")

note.pack()


root.mainloop()