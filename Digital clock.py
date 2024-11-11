''' Tkinter module is used for GUI( graphical User Interface) 
 mean user friend like button, labels,images etc'''

# import time module for current time, current date.
#strftime time: mean u can set date or time A/C to u.
# labels mean it will display text or image.


import tkinter as tk
from time  import strftime

root = tk.Tk() # creating object with help of tkinter.
root.title(" Hi People I'm Digital Clock")

def time():
  string = strftime('%H:%M:%S %p \n %D')
  label.config(text=string)
  label.after(1000,time)

label = tk.Label(root, font=('calibri',50,'bold'), background='green',foreground='black')
label.pack(anchor='center')  

time()

root.mainloop()



    


