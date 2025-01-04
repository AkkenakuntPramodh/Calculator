import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator")
window.geometry("370x720")
window.configure(bg="white")
history=["                 History              "]


frame_4 = tk.LabelFrame(window,width=340,height=500,bg="black")
frame_4.place(x=10,y=200)

entry_2 = tk.Entry(window,width=12,font=("Arial", 38),bg="black",fg="white",justify='right')
entry_2.place(x=20,y=30)


entry_1 = tk.Entry(window,width=12,font=("Arial", 38),bg="black",fg="white",justify='right')
entry_1.place(x=20,y=90)
entry_1.insert(0,0)


def one():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,1)
    else:   
        entry_1.insert(tk.END,1)
button_1=tk.Button(frame_4,text="1",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=one)
button_1.place(x=0,y=0)



def two():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,2)
    else:
        entry_1.insert(tk.END,2)
button_2=tk.Button(frame_4,text="2",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=two)
button_2.place(x=85,y=0)

def three():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,3)
    else:
        entry_1.insert(tk.END,3)
button_3=tk.Button(frame_4,text="3",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=three)
button_3.place(x=170,y=0)

def four():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,4)
    else:
        entry_1.insert(tk.END,4)
button_4=tk.Button(frame_4,text="4",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=four)
button_4.place(x=0,y=100)

def five():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,5)
    else:
        entry_1.insert(tk.END,5)

button_5=tk.Button(frame_4,text="5",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=five)
button_5.place(x=85,y=100)

def six():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,6)
    else:
        entry_1.insert(tk.END,6)
button_6=tk.Button(frame_4,text="6",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=six)
button_6.place(x=170,y=100)

def seven():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,7)
    else:
        entry_1.insert(tk.END,7)
button_7=tk.Button(frame_4,text="7",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=seven)
button_7.place(x=0,y=200)

def eight():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,8)
    else:
        entry_1.insert(tk.END,8)
button_8=tk.Button(frame_4,text="8",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=eight)
button_8.place(x=85,y=200)

def nine():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,9)
    else:
        entry_1.insert(tk.END,9)
button_9=tk.Button(frame_4,text="9",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=nine)
button_9.place(x=170,y=200)

def calculation():
    try:
        result = eval(entry_1.get())
        if type(result)== float:
            result = f"{result :.5f}"
        question = entry_1.get()
        value = f'{question}\n  ={result}'
        history.append(value)
        if question !='0':
            entry_2.delete(0, tk.END)
            entry_2.insert(0,question)
        
        entry_1.delete(0, tk.END)
        entry_1.insert(0, result)
    except:
        tk.messagebox.showerror("Error", "Invalid Expression.")
    
button_10=tk.Button(frame_4,text="=",font=("Arial", 12),fg="White", bg="green",width=7,height=4,borderwidth=5,command=calculation)
button_10.place(x=0,y=300)

def zero():
    result = entry_1.get()
    if result == '0':
        entry_1.delete(0, tk.END)
        entry_1.insert(0,0)
    else:
        entry_1.insert(tk.END,0)
button_11=tk.Button(frame_4,text="0",font=("Arial", 12),fg="White", bg="Indigo",width=7,height=4,borderwidth=5,command=zero)
button_11.place(x=85,y=300)


def clearing():
    entry_1.delete(0, tk.END)
    entry_1.insert(0,0)
button_12=tk.Button(frame_4,text="AC",font=("Arial", 12),fg="White", bg="red",width=7,height=4,borderwidth=5,command=clearing)
button_12.place(x=170,y=300)

def add():
    entry_1.insert(tk.END,"+")
button_13=tk.Button(frame_4,text="+",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=add)
button_13.place(x=255,y=0)

def subt():
    entry_1.insert(tk.END,"-")
button_14=tk.Button(frame_4,text="-",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=subt)
button_14.place(x=255,y=100)

def mult():
    entry_1.insert(tk.END,"*")
button_15=tk.Button(frame_4,text="x",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=mult)
button_15.place(x=255,y=200)


def div():
    entry_1.insert(tk.END,"/")
button_16=tk.Button(frame_4,text="/",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=div)
button_16.place(x=255,y=300)

def point():
    entry_1.insert(tk.END,".")
button_17=tk.Button(frame_4,text=".",font=("Arial", 32),fg="black", bg="lightyellow",width=2,borderwidth=5,command=point)
button_17.place(x=0,y=400)

def deleting():
    reading = entry_1.get()[:-1]
    entry_1.delete(0,tk.END)
    entry_1.insert(0,reading)
    if len(reading)==0:
        entry_1.insert(0,0)
button_18=tk.Button(frame_4,text="del",font=("Arial", 12),fg="white", bg="red",width=7,height=4,borderwidth=5,command=deleting)
button_18.place(x=75,y=400)

def left_bracket():
    entry_1.insert(tk.END,"(")
button_21=tk.Button(frame_4,text="(",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=left_bracket)
button_21.place(x=165,y=400)

def right_bracket():
    entry_1.insert(tk.END,")")
button_21=tk.Button(frame_4,text=")",font=("Arial", 12),fg="black", bg="lightyellow",width=7,height=4,borderwidth=5,command=right_bracket)
button_21.place(x=255,y=400)
    

def history_1():

    window.geometry("700x720")

    frame_2 = tk.LabelFrame(window,width=370,height=500)
    frame_2.place(x=400,y=30)

    def back():
        frame_2.destroy()
        window.geometry("370x720")
        
    button_20 = tk.Button(frame_2,text="X",bg="red",command=back)
    button_20.grid(row=0,column=100)
    
    for i in history:
        label = tk.Label(frame_2,text=i,font=24)
        label.grid()

button_19 = tk.Button(window,text="History",command=history_1)
button_19.place(x=300,y=160)
    


window.mainloop()
