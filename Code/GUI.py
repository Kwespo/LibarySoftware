import tkinter as tk
from tkinter import DISABLED, END, ttk
import sqlFunc as sql
import fileFunc as fileF

sqlCursor = sql.SQLFunc()
fileCursor = fileF.FileFunc()

class Gui():
    def __init__(self):
        pass
    
    

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("629x400")
    root.resizable(False, False)


    mainFrame = ttk.Frame(root)
    mainFrame.grid(column=0, row=0)

    # Listing the books
    docs = sqlCursor.docNames()
    docLabel = tk.Text(mainFrame)
    for i in range(len(docs)):
        docLabel.insert(END, docs[i][0] + "\n")
    docLabel.grid(column=1, row=2, rowspan=10, padx=10)
    docLabel.config(state=DISABLED, width=30, height=20, font=("Arial", 10))
    

    # Title
    title = ttk.Label(mainFrame, text="Library Management System", font=("Arial", 20))
    title.grid(column=0, row=1)
    title.config(padding = 10)

    # Search Label and entry    
    searchLabel = ttk.Label(mainFrame, text="Search for a file:", font=("Arial", 10))
    searchLabel.grid(column=0, row=2)
    searchEntry = ttk.Entry(mainFrame, width=30)

    def ff_Display():
        global fileCursor, sqlCursor, searchEntry
        guiDocName = searchEntry.get()
        file = sqlCursor.search_For_File(dName=guiDocName)
        print(file)
        # fileCursor.display_File(file[0][0])

    searchButton = ttk.Button(mainFrame, text="Search", command=lambda : ff_Display())
    searchButton.grid(column=0, row=4)

    tk.mainloop()

