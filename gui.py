import tkinter as tk
import random

root= tk.Tk()
root.title("Calcolatore")

canvas1 = tk.Canvas(root, width = 600, height = 600,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Simple Calculator')
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Inserisci un numero:')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(300, 140, window=entry1)

def getSquareRoot ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(300, 250, window=label3)
    
    label4 = tk.Label(root, text= round((float(x1)**0.5),2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 300, window=label4)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 200, window=button1)


def powerTwo():
    rand = entry1.get()
    label5 = tk.Label(root, text= int(rand)**2,font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 370, window=label5)
    
    
    
button2 = tk.Button(text='Alla seconda', command=powerTwo, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 330, window=button2)

root.mainloop()