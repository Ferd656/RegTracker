# -*- coding: utf-8 -*-

"""

    main.py
    created by: Ferdinand Feoli
    developer's profile: https://sites.google.com/view/ferdsprofile/
    python version: 3.7

    This module contains all features needed for the interaction of the user with the program.
    Includes the construction of the graphic interface.

"""

# External modules needed  - - - - - - -
import TkTreectrl
from tkinter import *
from bin import backend as bk
from PIL import ImageTk, Image
# - - - - - - - - - - - - - - - - - - - -

bk.create_readme()


class HyperlinkManager:
    """
        Defines hyperlink class.
        Adapted from code got from: http://effbot.org/zone/tkinter-text-hyperlink.htm
    """
    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="blue", underline=1)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, *args):
        if type(*args) != Event:
            print(type(*args))
        self.text.config(cursor="hand2")

    def _leave(self, *args):
        if type(*args) != Event:
            print(type(*args))
        self.text.config(cursor="")

    def _click(self, *args):
        if type(*args) != Event:
            print(type(*args))
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return


# =================== Root =============================================

root = Tk()

delay = StringVar()
delay.trace("w", lambda a, b, c:
            bk.entry_validation(entry, delay.get()))

root.wm_title(bk.myname)

rootwidth = 1000
rootheight = 390

root.geometry("{}x{}".format(rootwidth, rootheight))
root.resizable(width=False, height=False)

p_der = int(root.winfo_screenwidth()/2 - rootwidth/2)
p_baj = int(root.winfo_screenheight()/2 - rootheight/2)

root.geometry("+{}+{}".format(p_der, p_baj))

filename = PhotoImage(file=r"images\Background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.iconbitmap(r"images\RegMonitor.ico")


# =================== Frames ===========================================

frame1 = Frame(root, width=607, height=55,
               borderwidth=1, relief=RIDGE, bg="white")
frame1.pack()
frame1.place(x=275, y=5)

frame2 = Frame(root, width=250, height=55,
               borderwidth=1, relief=RIDGE, bg="white")
frame2.pack()
frame2.place(x=10, y=5)

frame3 = Frame(root, width=870, height=270)
frame3.place(x=10, y=88)

frame4 = Frame(frame3, width=870, height=270)
frame4.pack(fill=Y)

# =================== Buttons ==========================================

img = Image.open(r"images\Donate.png")
img = img.resize((60, 32), Image.ANTIALIAS)

bt_donate_pic = ImageTk.PhotoImage(img)

bt_donate = Button(frame1,  relief=FLAT, bg="white",
                   image=bt_donate_pic,
                   command=bk.donate)
bt_donate.place(x=516, y=8)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

img = Image.open(r"images\help.ico")
img = img.resize((32, 32), Image.ANTIALIAS)
bt_help_pic = ImageTk.PhotoImage(img)

bt_help = Button(frame1, relief=FLAT, bg="white",
                 image=bt_help_pic,
                 command=bk.html_readme)
bt_help.place(x=393, y=8)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

img = Image.open(r"images\favicon.ico")
img = img.resize((32, 32), Image.ANTIALIAS)
bt_database_pic = ImageTk.PhotoImage(img)

bt_database = Button(frame1, relief=FLAT, bg="white",
                     image=bt_database_pic,
                     command=bk.db_open)
bt_database.place(x=270, y=8)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

img = Image.open(r"images\regedit.ico")
img = img.resize((32, 32), Image.ANTIALIAS)
bt_regedit_pic = ImageTk.PhotoImage(img)

bt_regedit = Button(frame1, relief=FLAT, bg="white",
                    image=bt_regedit_pic,
                    command=bk.regedit_open)
bt_regedit.place(x=147, y=8)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

img = Image.open(r"images\log.ico")
img = img.resize((32, 32), Image.ANTIALIAS)
bt_log_pic = ImageTk.PhotoImage(img)

bt_log = Button(frame1, relief=FLAT, bg="white",
                image=bt_log_pic,
                command=bk.html_log)
bt_log.place(x=24, y=8)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

bt_run = Button(root, text="Run ►", width=8,
                font=("Helvetica", 10), fg="DodgerBlue4",
                command=lambda:
                bk.mainprocess(
                    root, monitor_txt,
                    listbox, int(delay.get())))
bt_run.place(x=915, y=310)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

bt_close = Button(root, text="Exit", width=6,
                  font=("Helvetica", 10), fg="firebrick4",
                  command=root.destroy)
bt_close.place(x=931, y=351)

# =================== Labels ===========================================

entry_lbl = Label(frame2, text="Define delay in seconds",
                  bg="White")
entry_lbl.place(x=10, y=2)

# =================== Text =============================================

help_txt = Text(frame2, relief=FLAT, bg="white",
                width=13, height=1,
                font=("Helvetica", 8))
help_txt.insert(INSERT, "(what is this?)",
                HyperlinkManager(help_txt).add(bk.explains_delay))
help_txt.place(x=142, y=2)

monitor_txt = Text(root, relief=SUNKEN, bg="gray21", fg="lime green",
                   width=124, height=1,
                   font=("Console", 9))
monitor_txt.insert(INSERT, "   Status:" + " "*100 +
                   "- -       click 'Run' button to start       - -")
monitor_txt.place(x=11, y=70)

# =================== Entries ==========================================

entry = Entry(frame2, textvariable=delay)
entry.insert(INSERT, "60")
entry.place(x=12, y=25)

# =================== List Boxes =======================================

listbox = TkTreectrl.MultiListbox(frame4, fg="midnight blue",
                                  width=870, height=270,
                                  command=lambda item:
                                  bk.get_listbox_selection(item,
                                                           listbox))
listbox.config(columns=('Key', 'Last time modified'))

listbox.column_config(0, width=658)
listbox.column_config(1, width=215)

listbox.pack(side="left", fill=BOTH)

scrollbar1 = Scrollbar(frame4, orient="vertical")
scrollbar1.config(command=listbox.yview)
scrollbar1.pack(side="right", fill="y")

scrollbar2 = Scrollbar(frame3, orient="horizontal")
scrollbar2.config(command=listbox.xview)
scrollbar2.pack(side="bottom", fill="x")

listbox.config(xscrollcommand=scrollbar2.set)
listbox.config(yscrollcommand=scrollbar1.set)


# ======================================================================

root.protocol("WM_DELETE_WINDOW", lambda: bk.close_protocol(root))

root.mainloop()
