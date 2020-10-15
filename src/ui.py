import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()

def requestFile():
  tk.messagebox.showinfo(title='Select file', message='Please select excel or csv file')
  
  filePath = (filedialog.askopenfile(filetypes=[('Excel file', '.xlsx .csv')])).name
  return filePath

def requestSheetName():
  tk.Label(root, text='Sheet Name').grid(row=0)
  sheetName = tk.Entry(root)
  tk.Button(
    root,
    text='OK',
    command=root.quit
  ).grid(
    row=3,
    column=0,
    sticky=tk.W,
    pady=4
  )
  sheetName.grid(row=0, column=1)
  root.mainloop()

  if len(sheetName.get()) < 1:
    return requestSheetName()
  else:
    return sheetName.get()