from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text

def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "You --> " + send + "\n")
    if bot is not None:
        text.insert(END, "AI Assistant <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def ask():
    ask_val = spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "You --> " + ask_val + "\n")
    if bot_val is not None:
        text.insert(END, "AI Assistant <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#FFFFFF")

Main_frame = LabelFrame(root, padx=50, pady=10, borderwidth=3, relief="raised", bg="#FFFFFF")
Main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew") 

Text_label = Label(Main_frame, text="AI Assistant", font=("Helvetica", 16, "bold"), bg="#FFFFFF")
Text_label.grid(row=0, column=1, padx=20, pady=10)

Display_Image = ImageTk.PhotoImage(Image.open("image/images.jpg"))
Image_Label = Label(Main_frame, image=Display_Image, bg="#FFFFFF")
Image_Label.grid(row=1, column=0, pady=30, padx= 30 , sticky="nsew")

text = Text(root, font=('Arial', 10), bg="#EFEFEF")
text.place(x=100, y=375, width=375, height=175)

entry1 = Entry(root, justify=CENTER)
entry1.place(x=100, y=560, width=350, height=30)

button1 = Button(root, text="Speak", bg="#4CAF50", fg="#FFFFFF", pady=10, padx=20, relief=FLAT, command=ask)
button1.place(x=100, y=610)

button2 = Button(root, text="Send", bg="#4CAF50", fg="#FFFFFF", pady=10, padx=20, relief=FLAT, command=User_send)
button2.place(x=250, y=610)

button3 = Button(root, text="Clear", bg="#4CAF50", fg="#FFFFFF", pady=10, padx=20, relief=FLAT, command=delete_text)
button3.place(x=400, y=610)

root.mainloop()
