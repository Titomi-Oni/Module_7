from tkinter import*

window = Tk()
window.title("Event Handeler")
window.geometry("100x100")

def handle_keypress(event):
    """Print The Character Associated To The Key Pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe Button Was Clicked!")

button = Button(text="Click Me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()