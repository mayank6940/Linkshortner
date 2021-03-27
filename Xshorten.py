import pyperclip
import pyshorteners
from tkinter import *

root = Tk()

root.geometry("1280x720")
root.title("URL SHORTENER")
root.configure(bg="#3D3C3A")

url = StringVar()
url_address = StringVar()


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
    url.set('')


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)
    url.set('')


Label(root, text="URL SHORTENER", font="arial 30 bold", bg='#0C423E', fg='#26C0DE').pack(pady=20)
Entry(root, textvariable=url, font="arial 30 bold", bg='#0C423E', fg='#26C0DE').pack(pady=20)
btn = Button(root, text="Generate Url", font='arial 30 bold', fg='#26C0DE', bg='#0C423E', command=urlshortener,
             border=0, )
btn.pack(pady=40)

Entry(root, textvariable=url_address, font='arial 30 bold', fg='#BCC6CC', bg='#0C423E').pack(pady=40)
Btn = Button(root, text="Copy URL", font='arial 30 bold', fg='#26C0DE', bg='#0C423E', command=copyurl, border=0, )
Btn.pack(pady=40)

root.mainloop()
