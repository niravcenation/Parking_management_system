from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
import easyocr
import datetime

root = Tk()
root.geometry("1000x800")
root.minsize(1000, 800)
root.maxsize(1000, 800)
root.title("Park-Up")


# root.configure(bg = 'yellow')

def two_wheel():
    f3 = Frame()
    f3.configure(bg="cyan")
    f3.place(x=0, y=0, width=1000, height=800)

    def click_1(args):
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext("no_plate.jpg")
        text1 = result[1][1]
        f = open("park_up.txt","a")
        if args == 1:
            lb1 = Label(f3, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb1.pack()
            lb1.place(x=50, y=445)
            f.write(f"The two-wheeler slot 1 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 2:
            lb2 = Label(f3, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb2.pack()
            lb2.place(x=50, y=590)
            f.write(f"The two-wheeler slot 2 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 3:
            lb3 = Label(f3, text="Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb3.pack()
            lb3.place(x=400, y=700)
            f.write(f"The two-wheeler slot 3 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 4:
            lb4 = Label(f3, text="Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb4.pack()
            lb4.place(x=560, y=700)
            f.write(f"The two-wheeler slot 4 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 5:
            lb5 = Label(f3, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb5.pack()
            lb5.place(x=800, y=445)
            f.write(f"The two-wheeler slot 5 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 6:
            lb6 = Label(f3, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb6.pack()
            lb6.place(x=800, y=590)
            f.write(f"The two-wheeler slot 6 with number-plate :{text1} at Time = {datetime.datetime.now()}" + "\n")
        else:
            tmsg.showwarning("Alert", "There are no Slots available\n You can contact to the Parking Manager")

    can_widget = Canvas(f3, width=1000, height=800, bg="cyan")

    l1 = Button(f3, text="Click here for Slot 1", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(1))
    l1.pack()
    l1.place(x=50, y=445)

    l2 = Button(f3, text="Click here for Slot 2", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(2))
    l2.pack()
    l2.place(x=50, y=590)

    l3 = Button(f3, text="Slot 3", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(3))
    l3.pack()
    l3.place(x=410, y=700)

    l4 = Button(f3, text="Slot 4", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(4))
    l4.pack()
    l4.place(x=570, y=700)

    l5 = Button(f3, text="Click here for Slot 5", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(5))
    l5.pack()
    l5.place(x=800, y=445)

    l6 = Button(f3, text="Click here for Slot 6", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_1(6))
    l6.pack()
    l6.place(x=800, y=590)

    l7 = Button(f3, text="If all slots are booked click here", borderwidth=5, font="TimesNewRoman 20 bold ",
                relief=RAISED, bg="green", command=lambda: click_1(7))
    l7.pack()
    l7.place(x=275, y=175)

    can_widget.pack()

    can_widget.create_rectangle(0, 0, 100, 50, fill="brown")
    can_widget.create_rectangle(0, 300, 100, 350, fill="brown")
    can_widget.create_text(75, 175, text="Entry", font="TimesNewRoman 40 bold")

    can_widget.create_rectangle(900, 0, 1000, 50, fill="brown")
    can_widget.create_rectangle(900, 300, 1000, 350, fill="brown")
    can_widget.create_text(925, 175, text="Exit", font="TimesNewRoman 40 bold")

    can_widget.create_rectangle(0, 400, 250, 410, fill="brown")
    can_widget.create_rectangle(0, 500, 250, 510, fill="brown")

    can_widget.create_rectangle(0, 550, 250, 560, fill="brown")
    can_widget.create_rectangle(0, 650, 250, 660, fill="brown")

    can_widget.create_rectangle(750, 400, 1000, 410, fill="brown")
    can_widget.create_rectangle(750, 500, 1000, 510, fill="brown")

    can_widget.create_rectangle(750, 550, 1000, 560, fill="brown")
    can_widget.create_rectangle(750, 650, 1000, 660, fill="brown")

    can_widget.create_rectangle(370, 600, 380, 800, fill="brown")
    can_widget.create_rectangle(480, 600, 490, 800, fill="brown")

    can_widget.create_rectangle(530, 600, 540, 800, fill="brown")
    can_widget.create_rectangle(640, 600, 650, 800, fill="brown")


def four_wheel():
    f2 = Frame()
    f2.configure(bg="cyan")
    f2.place(x=0, y=0, width=1000, height=800)

    def click_2(args):
        f = open("park_up.txt","a")
        reader1 = easyocr.Reader(['en'], gpu=False)
        result1 = reader1.readtext("no_plate.jpg")
        text2 = result1[1][1]
        if args == 1:
            lb1 = Label(f2, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb1.pack()
            lb1.place(x=50, y=490)
            f.write(f"The car slot 1 with number-plate : {text2} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 2:
            lb2 = Label(f2, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb2.pack()
            lb2.place(x=435, y=700)
            f.write(f"The car slot 2 with number-plate :{text2} at Time = {datetime.datetime.now()}" + "\n")
        elif args == 3:
            lb3 = Label(f2, text="This Slot is Booked", bg="red", fg="white", borderwidth=5, relief=RAISED, padx=5,
                        pady=5)
            lb3.pack()
            lb3.place(x=800, y=490)
            f.write(f"The car slot 3 with number-plate :{text2} at Time = {datetime.datetime.now()}" + "\n")
        else:
            tmsg.showwarning("Alert", "There are no Slots available\n You can contact to the Parking Manager")

    can_widget = Canvas(f2, width=1000, height=800, bg="cyan")

    l1 = Button(f2, text="Click here for Slot 1", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_2(1))
    l1.pack()
    l1.place(x=50, y=490)

    l2 = Button(f2, text="Click here for Slot 2", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_2(2))
    l2.pack()
    l2.place(x=435, y=700)

    l3 = Button(f2, text="Click here for Slot 3", borderwidth=5, relief=RAISED, bg="green", command=lambda: click_2(3))
    l3.pack()
    l3.place(x=800, y=490)

    l4 = Button(f2, text="If all slots are booked click here", borderwidth=5, font="TimesNewRoman 20 bold ",
                relief=RAISED, bg="green", command=lambda: click_2(4))
    l4.pack()
    l4.place(x=275, y=175)

    can_widget.pack()

    can_widget.create_rectangle(0, 0, 100, 50, fill="brown")
    can_widget.create_rectangle(0, 300, 100, 350, fill="brown")
    can_widget.create_text(75, 175, text="Entry", font="TimesNewRoman 40 bold")

    can_widget.create_rectangle(900, 0, 1000, 50, fill="brown")
    can_widget.create_rectangle(900, 300, 1000, 350, fill="brown")
    can_widget.create_text(925, 175, text="Exit", font="TimesNewRoman 40 bold")

    can_widget.create_rectangle(0, 400, 250, 410, fill="brown")
    can_widget.create_rectangle(0, 600, 250, 610, fill="brown")

    can_widget.create_rectangle(750, 400, 1000, 410, fill="brown")
    can_widget.create_rectangle(750, 600, 1000, 610, fill="brown")

    can_widget.create_rectangle(370, 600, 380, 800, fill="brown")
    can_widget.create_rectangle(600, 600, 610, 800, fill="brown")


def first_page():
    two_wheel()

    four_wheel()

    f1 = Frame()
    f1.configure(bg="cyan")
    f1.place(x=0, y=0, width=1000, height=800)

    Label(f1, text="What do you want to park?", font="TimesNewRoman 40 bold", bg="lightblue", fg="blue", borderwidth=10,
          relief=RIDGE, padx=15, pady=15).pack(side=TOP, fill="y", pady=30)

    Button(f1, text="Four Wheeler", font="TimesNewRoman 40 bold", command=four_wheel, bg="brown", fg="lightyellow",
           borderwidth=10, relief=SUNKEN).pack(side=TOP, pady=100)
    Button(f1, text="Two Wheeler", font="TimesNewRoman 40 bold", command=two_wheel, bg="brown", fg="lightyellow",
           borderwidth=10, relief=SUNKEN).pack(side=TOP, pady=100)


# def scan_page():
#     scan_frame = Frame()
#     scan_frame.configure(bg="yellow")
#     scan_frame.place(x=0, y=0, width=1000, height=800)
#
#     Label(scan_frame, text="Wait For A While To Scan Number-Plate", font="TimesNewRoman 20 bold", bg="lightblue",
#           fg="blue", pady=20,
#           padx=20,
#           borderwidth=10, relief=RIDGE).pack(side=TOP, pady=40)
#     reader = easyocr.Reader(['en'],gpu = False)
#     result = reader.readtext("no_plate.jpg")
#     text1 = result[1][1]
#     f = open("park_up.txt", "a")
#     f.write(f"The vehicle with number-plate{text1} at Time = {datetime.datetime.now()}" + "\n")
#
#     Label(scan_frame, text=f"The vehicle with number-plate{text1} at Time = {datetime.datetime.now()}",
#           font="TimesNewRoman 10 bold", bg="lightpink", fg="blue", pady=20,
#           padx=20,
#           borderwidth=10, relief=RIDGE).pack(side=TOP, pady=40)
#     Button(scan_frame, text="Your Number-Plate is Scanned.\nTap to Continue", font="TimesNewRoman 40 bold", command=first_page(),
#            bg="brown", fg="lightyellow",
#            borderwidth=10, relief=SUNKEN).pack(side=TOP, pady=100)


f0 = Frame()
f0.configure(bg="cyan")
f0.place(x=0, y=0, width=1000, height=800)

Label(f0, text="WELCOME TO THE PARKING ZONE", font="TimesNewRoman 20 bold", bg="lightblue", fg="blue", pady=20, padx=20,
      borderwidth=10, relief=RIDGE).pack(side=TOP, pady=40)
Label(f0, text="For Parking Tap the Below Image", font="TimesNewRoman 10 bold", bg="lightgreen", fg="red", pady=20,
      padx=20,
      borderwidth=10, relief=RIDGE).pack(side=TOP, pady=20)
image = Image.open("bg_img.png")
image = image.resize((700, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
lbl1 = Button(f0, image=photo, command=first_page, borderwidth=10, relief=RIDGE)
lbl1.pack()

root.mainloop()
