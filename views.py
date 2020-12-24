# !/usr/bin/env python3
from log_reader import all_logs, last_log
from tkinter import BOTH, END, HORIZONTAL, Tk, scrolledtext, ttk, filedialog, Label

root = Tk()
file_path = ''
l1 = Label(root, text="File path: ").place(x=350, y=450)


def get_file_path():
    global file_path
    global l1
    # Open and return file path
    file_path = filedialog.askopenfilename(title="Select A File", filetypes=(('log files', '*.log'),))
    # if l1 is Label:
    #     l1.destroy()
    # l1 = Label(root, text = "File path: " + file_path).place(x=350, y=450)


def main():
    def show_all_logs():
        console.configure(state='normal')  # enable insert
        console.insert(END, all_logs(file_path) + '\n')
        console.yview(END)  # autoscroll
        # console.configure(state='disabled')  # disable editing

    def show_last_logs():
        console.configure(state='normal')  # enable insert
        console.insert(END, last_log(file_path) + '\n')
        console.yview(END)  # autoscroll

    # root = Tk()
    root.title("Logs monitor")
    root.geometry("1000x800")
    ttk.Separator(root, orient=HORIZONTAL).pack(fill=BOTH)  # line in-between
    console = scrolledtext.ScrolledText(root, state='disable')
    console.config(width=1000)
    console.pack()
    ttk.Button(root, text='Show all logs', command=show_all_logs).place(x=0, y=450, height=200, width=100)
    ttk.Button(root, text='Show last logs', command=show_last_logs).place(x=100, y=450, height=200, width=110)
    ttk.Button(root, text='Clear window', command=lambda: console.delete(1.0, END)).place(x=210, y=450, height=200,
                                                                                          width=110)
    ttk.Button(root, text='Set path to log', command=get_file_path).place(x=320, y=450, height=200, width=110)
    root.mainloop()


if __name__ == '__main__':
    main()
