from pyrogram import Client
from tkinter import *

app = Client("my_account")


def write():
    i = 1000
    chat_id = id_entry.get()
    with app:
        while i > 1:
            i -= 7
            text = f'{i+7} - 7 = {i}'
            app.send_message(chat_id, text)

root = Tk()

root.title('1000-7 writer')
root.geometry('280x250')
root.resizable(width=False, height=False)

lable = Label(root, text='айдишник кому хотите ебануть:', font='Verdana 12')
id_entry = Entry(root, bg='white', font='Verdana 15')
button = Button(root, text='ебануть', font='Verdana 18', command=write)
lable.pack()
id_entry.pack()
button.place(x=80, y=280/2)

root.mainloop()