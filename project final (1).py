from functools import *
from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.configure(bg="#f8bbd0")
def imageguess():
    frame_option.destroy()
    framea=Frame(root, bg="red")
    framea.pack(side=TOP, fill=X)
    frameb=Frame(root, bg="skyblue")
    frameb.pack(side=TOP, fill=X)

    def animal():
        frameb.destroy()



        def clr():
            frameb.destroy()
            ani.destroy()
            butt.destroy()
            animal()

        ani=Frame(root, bg="pink")
        ani.pack(side=TOP, fill=X)
        butt=Frame(root, bg="pink")
        butt.pack(side=TOP, fill=X)
        flo=Frame(root, bg="pink")
        flo.pack(side=TOP)
        g=["dog","elephant","horse","lion","monkey","rabbit"]


        def check(inp):

            if name==inp:
                messagebox.showinfo("successfull","won the game")
                clr()

            else:
                messagebox.showinfo("failed","sorry wanna try again")




        name=random.choice(g)

        lab=Label(ani,width=700,height=350)
        img_loc="C:\\Users\\susheel\\Pictures\\New folder (2)\\"+name+".png"
        lab.img=PhotoImage(file=img_loc)
        lab["image"]=lab.img
        lab.pack()
        p="dog"
        but=Button(butt,text=p,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,p))
        q="elephant"
        but2=Button(butt,text=q,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,q))
        r="horse"
        but3=Button(butt,text=r,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,r))
        s="lion"
        but6=Button(butt,text=s,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,s))
        t="monkey"
        but4=Button(butt,text=t,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,t))
        u="rabbit"
        but5=Button(butt,text=u,font="verdana 20 bold italic",bg="orange",fg="black",bd=5,width=10,command=partial(check,u))
        but.pack(side=LEFT,padx=10)
        but2.pack(side=LEFT,padx=10)
        but3.pack(side=LEFT,padx=10)
        but4.pack(side=LEFT,padx=10)
        but5.pack(side=LEFT,padx=10)
        but6.pack(side=LEFT,padx=10)

    checkbox=Checkbutton(frameb,text="animals",bg="grey",font="verdana 40 bold italic",width=20,bd=6,fg="black",relief=RIDGE,command=animal)
    checkbox.pack()

frame_option=Frame(root)
frame_option.pack()
def start_the_game():
    frame_option.destroy()
    def cmr():
        fr.destroy()
        framea1.destroy()
        mainer.destroy()
    def check1(valt):
        a=valt
        b=str(val[pos])
        print('a is ',a,type(a))
        print('b is ',b,type(b))
        if(a==b):
            messagebox.showinfo("GUIDE","RIGHT ANSWER")
            buf.destroy()
            fr.destroy()
            clr1()
            start_the_game()
        else:
            messagebox.showinfo("GUIDE","wrong")
    def clr1():
        frame.destroy()
        frame1.destroy()
        frame4.destroy()
    clr1()
    li=["five","six","seven","one","two","three","four","eight","nine"]
    val=[5,6,7,1,2,3,4,8,9]
    copy_of_val=val[:]
    m=random.choice(li)
    pos=li.index(m)
    print(pos,li[pos],val[pos])
    fr=Frame(root,bg='black')
    fr.pack()
    la=Label(fr,text=m,bg="#80d9ff",fg="black",width=6,font=("verdana",80,"bold italic"),bd=5,relief=RAISED)
    la.pack(pady=30)
    mainer=Frame(root)
    mainer.pack()
    framea1=Frame(mainer)
    framea1.pack(fill=X)
    finlist=[]
    for i in range(7):
        b=random.choice(copy_of_val)
        finlist.append(b)
        copy_of_val.remove(b)
    #print(finlist)
    #print(copy_of_val)
    if (val[pos] in finlist):
        finlist.remove(val[pos])
    finlist.append(val[pos])
    bu=[]
    buf=Frame(root)
    buf.pack()
    for i in range(len(finlist)):
        for j in range(len(finlist)):
            p1=random.choice(finlist)
            finlist.remove(p1)
            bu.append(Button(buf,text=str(p1),font=('verdana 30 bold italic'),bd=5,relief=RAISED,bg='#9575cd',command=partial(check1,str(p1))))
            bu[-1].pack(side=LEFT)

def option():
    frame4.destroy()
    frame3.destroy()
    frame1.destroy()
    frame.destroy()

    b2=Button(frame_option,text="image guessing",bg="grey",fg="black",bd=5,font="algerian 40 bold italic",width=20,relief=RAISED,command=imageguess)
    b2.pack(side=BOTTOM)
    b3=Button(frame_option,text="number guessing",bg="grey",fg="black",bd=5,relief=RAISED,width=20,font="algerian 40 bold italic",command=start_the_game)
    b3.pack(side=BOTTOM)



def game():
    ans = messagebox.askquestion("guide", "let's start the game")
    if (ans == "yes"):
        option()
    else:
        exit()

frame3=Frame(root,bg="red")
frame3.pack(fill=X)
Frame_label=Label(frame3, text="welcome to kids learning game",bg="#f8bbd0",fg="black",font=("verdana",58,"bold italic"))
Frame_label.pack()
Frame_n=Label(frame3,text="number and image guessing game",bg="grey",fg="black",font=("verdana",34))
Frame_n.pack(fill=X)
frame=Frame(root,bg='#f8bbd0')
frame.pack(fill=X,pady=10)
label_1=Label(frame,text="Name      ",fg="white",bg="red",font=("verdana",30,"bold italic"),bd=4,relief=RAISED)
entry_1=Entry(frame,bg="purple",fg="white",font=("verdana",25,"bold"))
label_1.pack(side=LEFT,fill=X)
entry_1.pack(side=LEFT,padx=16)
frame1=Frame(root,bg='#f8bbd0')
frame1.pack(fill=X,pady=10)
label_2=Label(frame1,text="password ",fg="white",bg="red",font=("verdana",30,"bold italic"),bd=4,relief=RAISED)
entry_2=Entry(frame1,bg="purple",fg="white",font=("verdana",25,"bold"))
label_2.pack(side=LEFT,fill=X)
entry_2.pack(side=LEFT,padx=16)
frame4=Frame(root,bg='#f8bbd0')
frame4.pack(fill=X)
button=Button(frame4,text="start game",bg="grey",fg="white",bd=5,font=("verdana",20),relief=RIDGE,command=game)
button.pack(side=LEFT,pady=10)
root.mainloop()







