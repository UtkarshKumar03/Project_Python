from tkinter import *

first_num=second_num=operator=None

def click(num):
    current = entry_box['text']
    new = current + str(num)
    entry_box.config(text=new)
    
calculter = Tk()
calculter.geometry("299x380")
calculter.resizable(0,0)
calculter.configure(background= "#f7e7e7")
calculter.title("Simple Calculator")

entry_box = Label(calculter,text= '' ,bg= '#f7e7e7', fg= 'black')
entry_box.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
entry_box.config(font=("verdana",30,'bold'))

#Buttons
button = Button(calculter, text= '7', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(7))
button.grid(row=1,column=0)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '8', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(8))
button.grid(row=1,column=1)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '9', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(9))
button.grid(row=1,column=2)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '4', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(4))
button.grid(row=2,column=0)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '5', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(5))
button.grid(row=2,column=1)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '6', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(6))
button.grid(row=2,column=2)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '1', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(1))
button.grid(row=3,column=0)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '2', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(2))
button.grid(row=3,column=1)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '3', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(3))
button.grid(row=3,column=2)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '0', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:click(0))
button.grid(row=4,column=1)
button.config(font=("verdana",14,'bold'))

# Operators:
def cal_operators(op):
    global first_num,operator
    
    first_num = int(entry_box['text'])
    operator = op
    entry_box.config(text='')

button = Button(calculter, text= '+', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:cal_operators('+'))
button.grid(row=1,column=4)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '-', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:cal_operators('-'))
button.grid(row=2,column=4)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '*', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:cal_operators('*'))
button.grid(row=3,column=4)
button.config(font=("verdana",14,'bold'))

button = Button(calculter, text= '/', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda:cal_operators('/'))
button.grid(row=4,column=4)
button.config(font=("verdana",14,'bold'))

def equal():
    global first_num,second_num,operator
    second_num = int(entry_box['text'])
    if operator == "+":
        entry_box.config(text=str(first_num + second_num))
    elif operator == "-":
        entry_box.config(text=str(first_num - second_num))
    elif operator == "*":
        entry_box.config(text=str(first_num * second_num))
    else:
        if second_num == 0:
            entry_box.config(text='Error')
        else:
            entry_box.config(text=str(round(first_num / second_num)))
button = Button(calculter, text= '=', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= equal)
button.grid(row=4,column=2)
button.config(font=("verdana",14,'bold'))

def clear():
    entry_box.config(text='')
button = Button(calculter, text= 'CLEAR', width= 5, height= 2,bg= '#db9d9d',fg= 'black', command= lambda :clear())
button.grid(row=4,column=0)
button.config(font=("verdana",14,'bold'))

calculter.mainloop()