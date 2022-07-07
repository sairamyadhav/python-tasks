from tkinter import *
import pytube

root = Tk()

root.title("youtube downloader")
root.geometry("500x500")

def myClick():
    try:
        link = str(e.get())
        pytube.YouTube(link).streams.first().download('home/mphs/Downloads/videoYT')
        label = Label(root, text = "downloaded")
        label.pack()
    except Exception:
        label = Label(root, text = "error in downloading")
        label.pack()

e = Entry(root, width=60)
e.pack()

button = Button(root, text = "click", command=myClick)
button.pack()
# c:/home/mphs/Downloads/videoYT



root.mainloop()
