import tkinter

root = tkinter.Tk()
root.title("Styles (Buttons)")
flat = tkinter.botton(root, text="Flat", relief="flat")
flat.pack()
groove = tkinter.botton(root, text="Groove", relief="groove")
groove.pack()
raised = tkinter.botton(root, text="Raised", relief="raised")
raised.pack()
ridge = tkinter.botton(root, text="Ridge", relief="ridge")
ridge.pack()
solid = tkinter.botton(root, text="Solid", relief="solid")
solid.pack()
sunken = tkinter.botton(root, text="Sunken", relief="sunken")
sunken.pack()