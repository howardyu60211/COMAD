from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time

iner = Tk()
iner.title("password")

password = StringVar()
namechose = StringVar()
levelchose = IntVar()
password.set("")

def show(pd) :
    global password
    content = password.get()
    password.set(content + pd)

def backspace():
    global password
    password.set(str(password.get()[:-1]))

def goto_page(theip):
    notebook.config()
    if theip == Frame_in_notebook_1:
        notebook.add(Frame_in_notebook_1, text="1)確認帳戶",state="normal")
        notebook.add(Frame_in_notebook_2, text="2)輸入密碼",state="disabled")
        notebook.add(Frame_in_notebook_3, text="3)檢查密碼",state="disabled")
        notebook.select(theip)
    elif theip == Frame_in_notebook_2:
        notebook.add(Frame_in_notebook_1, text="1)確認帳戶",state="disabled")
        notebook.add(Frame_in_notebook_2, text="2)輸入密碼",state="normal")
        notebook.add(Frame_in_notebook_3, text="3)檢查密碼",state="disabled")
        notebook.select(theip)
    elif theip == Frame_in_notebook_3:
        notebook.add(Frame_in_notebook_1, text="1)確認帳戶",state="disabled")
        notebook.add(Frame_in_notebook_2, text="2)輸入密碼",state="disabled")
        notebook.add(Frame_in_notebook_3, text="3)檢查密碼",state="normal")
        notebook.select(theip)
        '''
        time.sleep(3)
        global password
        content = password.get()
        if content == "123456789" :
            print ("conform it !")
            iner.destroy()
        if content != "123456789" :
            print("wrong")
            notebook.add(Frame_in_notebook_1, text="1)確認帳戶",state="disabled")
            notebook.add(Frame_in_notebook_2, text="2)輸入密碼",state="normal")
            notebook.add(Frame_in_notebook_3, text="3)檢查密碼",state="disabled")
            notebook.select(Frame_in_notebook_3)
        '''
        

notebook = Notebook(iner)

Frame_in_notebook_1 = Frame()
name = Label(Frame_in_notebook_1,text="Name :").grid(row=0,column=0)
optionmenu = OptionMenu(Frame_in_notebook_1,namechose,"please choose name!!!","howard","yearn","wilson").grid(row=1,column=1)
level = Label(Frame_in_notebook_1,text="Level :").grid(row=2,column=0)
slider = Spinbox(Frame_in_notebook_1,from_=0,to=10,increment=1).grid(row=3,column=1)
btnconform = Button(Frame_in_notebook_1,text = "next >>>", width=10, command=lambda:goto_page(Frame_in_notebook_2)).grid(row=4,column=2)
notebook.add(Frame_in_notebook_1, text="1)確認帳戶")

Frame_in_notebook_2 = Frame()
lab_in_f2 = Label(Frame_in_notebook_2,textvariable=password,relief="raised",width=34).grid(row=0,column=0,columnspan=3)
bt1_in_f2 = Button(Frame_in_notebook_2,text = "1", width=10, command=lambda:show("1")).grid(row=1, column=0)
bt2_in_f2 = Button(Frame_in_notebook_2,text = "2", width=10, command=lambda:show("2")).grid(row=1, column=1)
bt3_in_f2 = Button(Frame_in_notebook_2,text = "3", width=10, command=lambda:show("3")).grid(row=1, column=2)
bt4_in_f2 = Button(Frame_in_notebook_2,text = "4", width=10, command=lambda:show("4")).grid(row=2, column=0)
bt5_in_f2 = Button(Frame_in_notebook_2,text = "5", width=10, command=lambda:show("5")).grid(row=2, column=1)
bt6_in_f2 = Button(Frame_in_notebook_2,text = "6", width=10, command=lambda:show("6")).grid(row=2, column=2)
bt7_in_f2 = Button(Frame_in_notebook_2,text = "7", width=10, command=lambda:show("7")).grid(row=3, column=0)
bt8_in_f2 = Button(Frame_in_notebook_2,text = "8", width=10, command=lambda:show("8")).grid(row=3, column=1)
bt9_in_f2 = Button(Frame_in_notebook_2,text = "9", width=10, command=lambda:show("9")).grid(row=3, column=2)
btnext_in_f2 = Button(Frame_in_notebook_2,text = "conform >>>", width=10, command=lambda:goto_page(Frame_in_notebook_3)).grid(row=4, column=0)
btdel_in_f2 = Button(Frame_in_notebook_2,text = "del", width=10, command=backspace).grid(row=4, column=1)
btback_in_2 = Button(Frame_in_notebook_2,text = "<<< back", width=10, command=lambda:goto_page(Frame_in_notebook_1)).grid(row=4, column=2)
notebook.add(Frame_in_notebook_2, text="2)輸入密碼",state="disabled")

Frame_in_notebook_3 = Frame()
checkpb = Progressbar(Frame_in_notebook_3,mode="determinate",length=200)
checkpb["maximum"] = 100
checkpb["value"] = 0
checkpb.start(interval=10)
checkpb.pack()
btback_in_f3 = Button(Frame_in_notebook_3,text = "<<< back", width=10, command=lambda:goto_page(Frame_in_notebook_2)).pack()
notebook.add(Frame_in_notebook_3, text="3)檢查密碼",state="disabled")
notebook.pack(padx = 20, pady = 20,fill = BOTH, expand=TRUE)
iner.mainloop()