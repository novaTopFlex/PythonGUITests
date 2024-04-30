import tkinter

# Note: This application is not intended to be taken seriously and is expressly intended as a demonstration for changing Tkinter window titles.

root = tkinter.Tk()

def tkA():
  root.configure(text="Test Window")

def tkB():
  root.configure(text="Demo Window")

def tkC():
  root.configure(text="Support")

def tkD():
  root.configure(text="Dictionary")

def tkE():
  root.configure(text="Documentation")

def tkF():
  root.configure(text="Editor")

def tkG():
  root.configure(text="Photo Editor")

def tkH():
  root.configure(text="Workstation")


buttonA = tkinter.Button(root, text="Change to Test Window", command=tkA)
buttonA.pack()
buttonB = tkinter.Button(root, text="Change to Demo Window", command=tkB)
buttonB.pack()
buttonC = tkinter.Button(root, text="Change to Support", command=tkC)
buttonC.pack()
buttonD = tkinter.Button(root, text="Change to Dictionary", command=tkD)
buttonD.pack()
buttonE = tkinter.Button(root, text="Change to Documentation", command=tkE)
buttonE.pack()
buttonF = tkinter.Button(root, text="Change to Editor", command=tkF)
buttonF.pack()
buttonG = tkinter.Button(root, text="Change to Photo Editor", command=tkG)
buttonG.pack()
buttonH = tkinter.Button(root, text="Change to Workstation", command=tkH)
buttonH.pack()
root.mainloop()
