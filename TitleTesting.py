import tkinter

# Note: This application is not intended to be taken seriously and is expressly intended as a demonstration for changing Tkinter window titles.

root = tkinter.Tk()

def tkA():
  root.title("Test Window")

def tkB():
  root.title("Demo Window")

def tkC():
  root.title("Support")

def tkD():
  root.title("Dictionary")

def tkE():
  root.title("Documentation")

def tkF():
  root.title("Editor")

def tkG():
  root.title("Photo Editor")

def tkH():
  root.title("Workstation")


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
