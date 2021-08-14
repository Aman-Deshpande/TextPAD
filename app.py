from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import colorchooser
import tkinter.messagebox as m
# import win32print
# import win32api


# Creating splash screen
splash_root = Tk()
splash_root.title("TextPAD")
splash_root.geometry("655x585")
splash_root.iconbitmap('notepad.ico')
splash_root.config(bg="orange")
# bg = PhotoImage(file="textbgimg.jpg")


def step():
    progress_bar['value'] += 20
    progress_bar.start(10)
    # Splash Screen Timer
    splash_root.after(1150, main_TextPAD)   # calling the main_TEXTPAD function


# Creating a progress bar
progress_bar = ttk.Progressbar(splash_root, orient=HORIZONTAL, length=450,
                               mode='determinate')  # here determinate means a complete bar
progress_bar.place(x=100, y=410)
button = Button(splash_root, text="Open TextPAD", command=step)
button.place(x=265, y=450)

# Adds the label TEXTPAD
splash_label = Label(splash_root, text="TextPAD", font=("Times", 50, "italic"))
splash_label.place(x=200, y=190)


def main_TextPAD():
    splash_root.destroy()  # killing splash screen

    # Entering the main TextPAD
    root = Tk()
    root.title("Untitled-TextPAD")
    root.iconbitmap('notepad.ico')
    root.geometry("655x585")
# _____________________________________________________
    # CREATING ALL THE FUNCTIONS
    # CREATING NEW FILE
    # Functions of MENUBAR

    def newfile():
        # This will delete the previous file's text from text area
        my_text.delete(1.0, END)
        # delete(1.0, END) means delete all text from line 1 till END
        root.title("New File-TextPAD")
        status_bar.config(text="New File")  # updating status bar

    # OPENING A NEW FILE
    def openfile():
        my_text.delete(1.0, END)  # Deletes previous text
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All files", "*.*"), ("Text Documents", "*.txt"), ("Python Files", "*.py")])
        name = file
        # This specifies All files means that it will accept extensions of all file and
        # for text documents it will accept for .txt
        status_bar.config(text=name)
        if file == "":
            file = None
        else:
            # This function will only get the name of the file from full path
            root.title(os.path.basename(file) + "-Notepad")
            my_text.delete(1.0, END)
            f = open(file, "r")  # File IO basics(opening file in read mode)
            # will insert all the character from column 1 till where f.read() ends
            my_text.insert(1.0, f.read())
            f.close()

    # Save As function
    def saveas():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:\Textpad", title="Save File",
                                                 filetypes=(
                                                     ("Text Files",
                                                      "*.txt"), ("HTML Files", "*.html"),
                                                     ("All Files", "*.*")))
        if text_file:
            name1 = text_file
            root.title(os.path.basename(text_file) + "-Notepad")
            status_bar.config(text=f"{name1} - SAVED!!")
            m.showinfo("Status", "File Saved")

        # save the file
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()

    # save function
    def save():
        pass

    # Adding function from EDIT menu
    def cut():
        my_text.event_generate("<<Cut>>")

    def copy():
        my_text.event_generate("<<Copy>>")

    def paste():
        my_text.event_generate("<<Paste>>")

    def bold():
        bold1 = font.Font(my_text, my_text.cget("font"))
        bold1.configure(weight="bold")

        # configure a tag
        my_text.tag_configure("bold", font=bold1)

        # define current_tag
        current_tags = my_text.tag_names("sel.first")

        if "bold" in current_tags:
            my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
            my_text.tag_add("bold", "sel.first", "sel.last")

    def italics():
        italic = font.Font(my_text, my_text.cget("font"))
        italic.configure(slant="italic")

        # configure a tag
        my_text.tag_configure("italic", font=italic)

        # define current_tag
        current_tags = my_text.tag_names("sel.first")

        if "italic" in current_tags:
            my_text.tag_remove("italic", "sel.first", "sel.last")
        else:
            my_text.tag_add("italic", "sel.first", "sel.last")

    def color():
        # pick a color
        my_color = colorchooser.askcolor()[1]
        if my_color:
            colorfont = font.Font(my_text, my_text.cget("font"))

            # configure a tag
            my_text.tag_configure(
                "colored", font=colorfont, foreground=my_color)

            # define current_tag
            current_tags = my_text.tag_names("sel.first")

            if "colored" in current_tags:
                my_text.tag_remove("colored", "sel.first", "sel.last")
            else:
                my_text.tag_add("colored", "sel.first", "sel.last")

    def bg_color():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            my_text.config(bg=my_color)

    def all_textcolor():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            my_text.config(fg=my_color)

    def addimage():
        global im
        position = my_text.index(INSERT)
        image = askopenfilename(defaultextension=".png",
                                filetypes=[("png", "*.png"), ("jpeg", "*.jpg")])
        im = PhotoImage(file=image)
        my_text.image_create(position, image=im)

    def selectall():
        # Adding Tag to select all text
        my_text.tag_add('sel', '1.0', 'end')

    def clearall():
        my_text.delete(1.0, END)

    def night_mode():
        color1 = "#000000"  # Black color hex code
        color2 = "#373737"  # Dark grey
        text_color = "white"

        root.config(bg="black")
        status_bar.config(bg=color2, fg=text_color)
        my_text.config(bg=color2, fg=text_color)
        toolbar_frame.config(bg=color2)
        # toolbar buttons
        redo_b.config(bg=color2, fg=text_color)
        undo_b.config(bg=color2, fg=text_color)
        color_text.config(bg=color2, fg=text_color)
        add_image.config(bg=color2, fg=text_color)
        mode.config(bg=color2, fg=text_color)
        # Changing drop down menus
        file_menu.config(bg=color2, fg=text_color)
        edit_menu.config(bg=color2, fg=text_color)
        font_menu.config(bg=color2, fg=text_color)
        color_menu.config(bg=color2, fg=text_color)
        r_menu.config(bg=color2, fg=text_color)

    def night_modeoff():
        color1 = "SystemButtonFace"
        color2 = "black"
        text_color = "black"

        root.config(bg="white")
        status_bar.config(bg="white", fg="black")
        my_text.config(bg="white", fg="black")
        toolbar_frame.config(bg="white")
        # toolbar buttons
        redo_b.config(bg=color1, fg=color2)
        undo_b.config(bg=color1, fg=color2)
        color_text.config(bg=color1, fg=color2)
        add_image.config(bg=color1, fg=color2)
        mode.config(bg=color1, fg=color2)
        # Changing drop down menus
        file_menu.config(bg=color1, fg=color2)
        edit_menu.config(bg=color1, fg=color2)
        font_menu.config(bg=color1, fg=color2)
        color_menu.config(bg=color1, fg=color2)
        r_menu.config(bg=color1, fg=color2)

    # right click menu
    def popup(event):
        r_menu.tk_popup(event.x_root,
                        event.y_root)  # This function will popup the menu in brackets are the coordinates where to popup the menu

    def about():
        m.showinfo("TextPAD",
                   "TextPAD by Group 4 - G2 Batch \n\n 7037 Utkarsh Mahadik \n 7038 Aman Deshpande \n 7039 Saiprasad Mane \n 7040 Rushikesh Dudhal")

    def rateUs():
        root1 = Tk()
        root1.geometry("230x120")
        root1.title("TextPAD")
        root.iconbitmap('notepad.ico')
        slider = Scale(root1, from_=0, to=5, orient=HORIZONTAL)
        Label(root1, text="How was your experience?").pack()
        slider.pack()
        Button(root1, text="Submit", command=submit).pack()

    def submit():
        m.showinfo("User experience", f"Thanks for the rating ")
# ______________________________________________________________________________

    # create a tool bar frame
    toolbar_frame = Frame(root)
    toolbar_frame.pack(fill=X)

    # Creating mainframe
    my_frame = Frame(root)
    my_frame.pack(pady=5)

    # creating scrollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # Horizontal scrollbar
    hor_scroll = Scrollbar(my_frame, orient='horizontal')
    hor_scroll.pack(side=BOTTOM, fill=X)

    # Creating textbox
    my_text = Text(my_frame, font=("Consolas", 13), selectbackground="lightblue",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
    my_text.pack(fill=BOTH)
    text_scroll.config(command=my_text.yview)  # configuring the text box
    hor_scroll.config(command=my_text.xview)

    # Creating MENU
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Adding file menu
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=newfile)
    file_menu.add_command(label="Open", command=openfile)
    file_menu.add_command(label="Save", command=save)
    file_menu.add_command(label="Save As", command=saveas)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Add edit menu
    edit_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut, accelerator="Ctrl+x")
    edit_menu.add_command(label="Copy", command=copy, accelerator="Ctrl+c")
    edit_menu.add_command(label="Paste", command=paste, accelerator="Ctrl+v")
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Undo", command=my_text.edit_undo, accelerator="Ctrl+z")
    edit_menu.add_command(
        label="Redo", command=my_text.edit_redo, accelerator="Ctrl+y")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All",
                          command=selectall, accelerator="Ctrl+a")
    edit_menu.add_command(label="Clear All", command=clearall)

    # Add Font menu
    font_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Font", menu=font_menu)
    font_menu.add_cascade(label="Bold", command=bold)
    font_menu.add_cascade(label="Italics", command=italics)

    # Add color Menu
    color_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Color", menu=color_menu)
    color_menu.add_cascade(label="Selected Text", command=color)
    color_menu.add_cascade(label="All Text", command=all_textcolor)
    color_menu.add_cascade(label="Background", command=bg_color)

    # ADDing menu for Night mode
    mode = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Night Mode", menu=mode)
    mode.add_cascade(label="Night Mode ON", command=night_mode)
    mode.add_cascade(label="Night Mode OFF", command=night_modeoff)

    # Help Menu
    help = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=help)
    help.add_command(label="View Help")
    help.add_command(label="About TextPAD", command=about)
    help.add_separator()
    help.add_command(label="Rate Us", command=rateUs)

    # Add statusbar at Bottom
    status_bar = Label(root, text='Ready', anchor="w")
    status_bar.pack(fill=X, side=BOTTOM, ipady=10)

    # creating button of toolbar
    undo_b = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
    redo_b = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
    undo_b.grid(row=0, column=0, sticky=W, padx=5, pady=1)
    redo_b.grid(row=0, column=1)
    # Text color
    color_text = Button(toolbar_frame, text="Text Color", command=color)
    color_text.grid(row=0, column=2, padx=5, pady=1)
    # Add Image button
    add_image = Button(toolbar_frame, text="Insert Image", command=addimage)
    add_image.grid(row=0, column=3, padx=5, pady=1)

    # Creating Menu on Right
    r_menu = Menu(my_text, tearoff=0)
    r_menu.add_command(label="Cut", command=cut)
    r_menu.add_command(label="Copy", command=copy)
    r_menu.add_command(label="Paste", command=paste)
    r_menu.add_separator()
    r_menu.add_command(label="Undo", command=my_text.edit_undo)
    r_menu.add_command(label="Redo", command=my_text.edit_redo)
    r_menu.add_separator()
    r_menu.add_command(label="Select All", command=selectall)
    r_menu.add_command(label="Clear All", command=clearall)
    r_menu.add_separator()
    r_menu.add_command(label="Exit", command=root.quit)
    root.bind("<Button-3>", popup)


mainloop()
