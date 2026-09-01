from tkinter import *
from datetime import date

root = Tk()
root_title = "Workshop Participant Greeting"
root.geometry  =("400 x 300")

heading = Label(
    text = "Workshop Welcome Desk",
    fg = "white",
    bg = "072F5F",
    height =1,
    width = 300
)

name_label = Label(
    text ="Participant Name",
    bg ="#74EDE5"
)
name_entry = Entry()

def display_welcome():
    name = name_entry.get()