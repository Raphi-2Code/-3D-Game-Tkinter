from tkinter import *
import tkinter.messagebox
root = Tk(className="3D Game")
c=Canvas(root)
c.pack()
frameCnt = 58
def do_time():
    global not_timeout
    not_timeout=True
Button(root,text="protect",command=do_time).pack()
frames = [PhotoImage(file='pygif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
__round=1
r=0
not_timeout=False
level=0
def update(ind):
    global k,__round,level,r,time,not_timeout
    frame = frames[ind]
    ind += 1
    if ind>=frameCnt:
        ind=0
        __round+=1
    c.itemconfig(character, image=frame)
    k+=1.4 if __round>=2 else 0
    if k>round(float(c.cget("height"))) and __round==r+1:
        k=-100
        not_timeout=False
    if not_timeout==False:
        c.itemconfig(p,fill="red")
    if 130<round(k)>60 and not_timeout==False:
        #c.create_text(100,100, text="You died! :(")
        #c.create_text(100,100, text=f"\n\nYou reached level: {level}")
        tkinter.messagebox.showinfo("",f"You died! :(\nYou reached level: {level}")
        exit()
    level+=1
    if not_timeout==True:
        c.itemconfig(p,fill="silver")
    c.coords(p,100,k)
    r=__round
    root.after(2, update, ind)
character = c.create_image((100,100), image=frames[0])
k=-100
p=c.create_text(100,k,text="X",font="Arial 25",fill="red")#"#09FF15")#▲ silver geht sogar!
root.after(0, update, 0)
root.mainloop()
