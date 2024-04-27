import tkinter
import tkinter.ttk

root = tkinter.Tk()
notes = tkinter.ttk.Notebook(root)
notes.pack()
tabA = tkinter.ttk.Frame(root)
notes.add(tabA, text="Cursors 1-10")
tabB = tkinter.ttk.Frame(root)
notes.add(tabB, text="Cursors 11-20")
tabC = tkinter.ttk.Frame(root)
notes.add(tabC, text="Cursors 21-30")
tabD = tkinter.ttk.Frame(root)
notes.add(tabD, text="Cursors 31-40")
tabE = tkinter.ttk.Frame(root)
notes.add(tabE, text="Cursors 41-50")
tabF = tkinter.ttk.Frame(root)
notes.add(tabF, text="Cursors 51-60")
def cursor0():
  root.configure(cursor="X_cursor")

bt0 = tkinter.Button(tabA, text="X_cursor", command=cursor0)
bt0.pack()

def cursor1():
  root.configure(cursor="arrow")

bt1 = tkinter.Button(tabA, text="arrow", command=cursor1)
bt1.pack()

def cursor2():
  root.configure(cursor="based_arrow_down")

bt2 = tkinter.Button(tabA, text="based_arrow_down", command=cursor2)
bt2.pack()

def cursor3():
  root.configure(cursor="based_arrow_up")

bt3 = tkinter.Button(tabA, text="based_arrow_up", command=cursor3)
bt3.pack()

def cursor4():
  root.configure(cursor="boat")

bt4 = tkinter.Button(tabA, text="boat", command=cursor4)
bt4.pack()

def cursor5():
  root.configure(cursor="bogosity")

bt5 = tkinter.Button(tabA, text="bogosity", command=cursor5)
bt5.pack()

def cursor6():
  root.configure(cursor="bottom_left_corner")

bt6 = tkinter.Button(tabA, text="bottom_left_corner", command=cursor6)
bt6.pack()


def cursor7():
  root.configure(cursor="bottom_right_corner")

bt7 = tkinter.Button(tabA, text="bottom_right_corner", command=cursor7)
bt7.pack()


def cursor8():
  root.configure(cursor="bottom_side")

bt8 = tkinter.Button(tabA, text="bottom_side", command=cursor8)
bt8.pack()


def cursor9():
  root.configure(cursor="bottom_tee")

bt9 = tkinter.Button(tabA, text="bottom_tee", command=cursor9)
bt9.pack()

def cursorA():
  root.configure(cursor="box_spiral")

btA = tkinter.Button(tabB, text="box_spiral", command=cursorA)
btA.pack()

def cursorB():
  root.configure(cursor="center_ptr")

btB = tkinter.Button(tabB, text="center_ptr", command=cursorB)
btB.pack()

def cursorC():
  root.configure(cursor="circle")

btC = tkinter.Button(tabB, text="circle", command=cursorC)
btC.pack()

def cursorD():
  root.configure(cursor="clock")

btD = tkinter.Button(tabB, text="clock", command=cursorD)
btD.pack()

def cursorE():
  root.configure(cursor="coffee_mug")

btE = tkinter.Button(tabB, text="coffee_mug", command=cursorE)
btE.pack()

def cursorF():
  root.configure(cursor="cross")

btF = tkinter.Button(tabB, text="cross", command=cursorF)
btF.pack()

def cursorG():
  root.configure(cursor="cross_reverse")

btG = tkinter.Button(tabB, text="cross_reverse", command=cursorG)
btG.pack()

def cursorH():
  root.configure(cursor="crosshair")

btH = tkinter.Button(tabB, text="crosshair", command=cursorH)
btH.pack()

def cursorI():
  root.configure(cursor="diamond_cross")

btI = tkinter.Button(tabB, text="diamond_cross", command=cursorI)
btI.pack()

def cursorJ():
  root.configure(cursor="dot")

btJ = tkinter.Button(tabB, text="dot", command=cursorJ)
btJ.pack()

def cursorK():
  root.configure(cursor="dotbox")

btK = tkinter.Button(tabC, text="dotbox", command=cursorK)
btK.pack()

def cursorL():
  root.configure(cursor="double_arrow")

btL = tkinter.Button(tabC, text="double_arrow", command=cursorL)
btL.pack()

def cursorM():
  root.configure(cursor="draft_large")

btM = tkinter.Button(tabC, text="draft_large", command=cursorM)
btM.pack()

def cursorN():
  root.configure(cursor="draft_small")

btN = tkinter.Button(tabC, text="draft_small", command=cursorN)
btN.pack()

def cursorO():
  root.configure(cursor="draped_box")

btO = tkinter.Button(tabC, text="draped_box", command=cursorO)
btO.pack()

def cursorP():
  root.configure(cursor="exchange")

btP = tkinter.Button(tabC, text="exchange", command=cursorP)
btP.pack()

def cursorQ():
  root.configure(cursor="fleur")

btQ = tkinter.Button(tabC, text="fleur", command=cursorQ)
btQ.pack()

def cursorR():
  root.configure(cursor="gobbler")

btR = tkinter.Button(tabC, text="gobbler", command=cursorR)
btR.pack()

def cursorS():
  root.configure(cursor="gumby")

btS = tkinter.Button(tabC, text="gumby", command=cursorS)
btS.pack()

def cursorT():
  root.configure(cursor="hand1")

btT = tkinter.Button(tabC, text="hand1", command=cursorT)
btT.pack()

def cursorU():
  root.configure(cursor="hand2")

btU = tkinter.Button(root, text="hand2", command=cursorU)
btU.pack()

def cursorV():
  root.configure(cursor="heart")

btV = tkinter.Button(root, text="heart", command=cursorV)
btV.pack()

def cursorW():
  root.configure(cursor="icon")

btW = tkinter.Button(root, text="icon", command=cursorW)
btW.pack()

def cursorX():
  root.configure(cursor="iron_cross")

btX = tkinter.Button(root, text="iron_cross", command=cursorX)
btX.pack()

def cursorY():
  root.configure(cursor="left_ptr")

btY = tkinter.Button(root, text="left_ptr", command=cursorY)
btY.pack()

def cursorZ():
  root.configure(cursor="left_side")

btZ = tkinter.Button(root, text="left_side", command=cursorZ)
btZ.pack()

def cursor10():
  root.configure(cursor="left_tee")

bt10 = tkinter.Button(root, text="left_tee", command=cursor10)
bt10.pack()

def cursor11():
  root.configure(cursor="leftbutton")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor12():
  root.configure(cursor="ll_angle")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor13():
  root.configure(cursor="lr_angle")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor14():
  root.configure(cursor="man")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor15():
  root.configure(cursor="middlebutton")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor16():
  root.configure(cursor="mouse")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor17():
  root.configure(cursor="none")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor18():
  root.configure(cursor="pencil")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor19():
  root.configure(cursor="pirate")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor20():
  root.configure(cursor="plus")

bt5 = tkinter.Button(root, text="bogosity", command=cursor20)
bt5.pack()

def cursor21():
  root.configure(cursor="question_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor21)
bt5.pack()

def cursor22():
  root.configure(cursor="right_ptr")

bt5 = tkinter.Button(root, text="bogosity", command=cursor22)
bt5.pack()

def cursor23():
  root.configure(cursor="right_side")

bt5 = tkinter.Button(root, text="bogosity", command=cursor23)
bt5.pack()

def cursor24():
  root.configure(cursor="right_tee")

bt5 = tkinter.Button(root, text="bogosity", command=cursor24)
bt5.pack()

def cursor25():
  root.configure(cursor="rightbutton")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor26():
  root.configure(cursor="rtl_logo")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor27():
  root.configure(cursor="sailboat")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor28():
  root.configure(cursor="sb_down_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor29():
  root.configure(cursor="sb_h_double_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor30():
  root.configure(cursor="sb_left_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor31():
  root.configure(cursor="sb_right_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor32():
  root.configure(cursor="sb_up_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor33():
  root.configure(cursor="sb_v_double_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor34():
  root.configure(cursor="shuttle")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor35():
  root.configure(cursor="sizing")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor36():
  root.configure(cursor="spider")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor37():
  root.configure(cursor="spraycan")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor38():
  root.configure(cursor="star")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor39():
  root.configure(cursor="target")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor40():
  root.configure(cursor="tcross")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor41():
  root.configure(cursor="top_left_arrow")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor42():
  root.configure(cursor="top_left_corner")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor43():
  root.configure(cursor="top_right_corner")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor44():
  root.configure(cursor="top_side")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor45():
  root.configure(cursor="top_tee")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor46():
  root.configure(cursor="trek")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor47():
  root.configure(cursor="ul_angle")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor48():
  root.configure(cursor="umbrella")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor49():
  root.configure(cursor="ur_angle")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor50():
  root.configure(cursor="watch")

bt5 = tkinter.Button(root, text="bogosity", command=cursor5)
bt5.pack()

def cursor51():
  root.configure(cursor="xterm")

bt51 = tkinter.Button(root, text="xterm", command=cursor51)
bt51.pack()

root.mainloop()
