from tkinter import *
from googletrans import Translator


def trans():
    text = rus.get(1.0, END)
    result = translator.translate(text, dest="en")
    eng.delete(1.0, END)
    eng.insert(1.0, result.text)
    rus.delete(1.0, END)


root = Tk()
root.geometry("500x350")
root.title("Переводчик")
root.resizable(width=False, height=False)
root["background"] = "grey"
translator = Translator()

label = Label(
    root,
    text="Введите текст на русском языке",
    font="Arial 15 bold",
    bg="grey",
    fg="black",
)
label.place(relx=0.5, y=30, anchor=CENTER)
rus = Text(root, width=35, height=5, font="Arial 12 bold")
rus.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text="Перевести", command=trans)
btn.place(relx=0.5, y=180, anchor=CENTER)

eng = Text(root, width=35, height=5, font="Arial 12 bold")
eng.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()