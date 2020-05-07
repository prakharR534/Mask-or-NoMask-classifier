from tkinter import * 
#from tkinter.ttk import *
from tkinter.filedialog import askopenfile


root = Tk()
root.title('project title')
root.geometry('1200x500')

def open_file():
	file = askopenfile(mode = 'r', filetypes=[('Python Files', '*.py')])
	


w = Label(root, text ='Welcome',font = "Helvetica 50")
w.pack(side = TOP, pady = 20)

label_result = Label(root, text = ' Result ' , font = "Helvetica 16").place(x=1000,y=100)


#submit_button1 = Button(root, text ='Open', command = lambda:open_file()) 
#submit_button1.pack(side = TOP, pady = 10) 

submit_button1 = Button(root,text = 'Browse/open',command = lambda:open_file(),height=3,width=16).place(x=40,y=100)
submit_button2 = Button(root,text = 'submit2',height=3,width=16).place(x=40,y=200)
submit_button3 = Button(root,text = 'START/PREDICT',height=3,width=16).place(x=40,y=300)



clear_button1 = Button(root,text = 'Clear1',height=2,width=16).place(x=800,y=400)
clear_button2 = Button(root,text = 'Clear2',height=2,width=16).place(x=1000,y=400)
root.mainloop()
