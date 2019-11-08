import tkinter as tk
from tkinter import Tk
import math


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #describing the window itself
        self.parent.title("Plate Calculator")
        self.parent.configure(background="red")
        self.parent.geometry("500x500")
        #prompting label
        self.lbl = tk.Label(parent, text = "Enter the desired weight below:", bg ="red", font = ("Arial Bold", 20))
        self.lbl.grid(column = 0, row = 1, sticky = tk.W)
        #entry box
        self.entry = tk.Entry(parent)
        self.entry.grid(column = 0, row = 2, sticky = tk.W)
        self.entry.focus()
        #buttons
        self.btn1 = tk.Button(parent, text = "Calculate", bg = "red", fg = "black", command =lambda: self.clicked(), font = ("Arial", 20))
        self.btn1.grid(column = 0, row = 3, sticky = tk.W)
        self.btn2 = tk.Button(parent, text = "Exit", bg = "red", fg = "black", command =lambda: exit(), font = ("Arial", 20))
        self.btn2.grid(column = 0, row = 4, sticky = tk.W)
        #constant output labels
        self.lbla = tk.Label(parent, text = "45lb Plate(s): ", bg ="red", font = ("Arial Bold", 20))
        self.lbla.grid(column = 0, row = 6, sticky = tk.W)
        self.lblb = tk.Label(parent, text = "25lb Plate(s): ", bg ="red", font = ("Arial Bold", 20))
        self.lblb.grid(column = 0, row = 7, sticky = tk.W)
        self.lblc = tk.Label(parent, text = "10lb Plate(s): ", bg ="red", font = ("Arial Bold", 20))
        self.lblc.grid(column = 0, row = 8, sticky = tk.W)
        self.lbld = tk.Label(parent, text = "5lb Plate(s): ", bg ="red", font = ("Arial Bold", 20))
        self.lbld.grid(column = 0, row = 9, sticky = tk.W)
        self.lble = tk.Label(parent, text = "2.5lb Plate(s): ", bg ="red", font = ("Arial Bold", 20))
        self.lble.grid(column = 0, row = 10, sticky = tk.W)
        #variable output labels
        self.lbl1 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl1.grid(column = 1, row = 6, sticky = tk.W)
        self.lbl2 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl2.grid(column = 1, row = 7, sticky = tk.W)
        self.lbl3 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl3.grid(column = 1, row = 8, sticky = tk.W)
        self.lbl4 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl4.grid(column = 1, row = 9, sticky = tk.W)
        self.lbl5 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl5.grid(column = 1, row = 10, sticky = tk.W)        
 
    def clicked(self):
        '''Button click event: Performs a series of calculations on the value entered into
        the entry box, then displays those to labels'''
        out = self.entry.get()#saves value in entry box to a variable
        int_out = int(out)#converts that to an integer and saves to a new variable
        self.wghtRndd = 5 * round(int_out/5) #rounds the weight to the nearest 5lb increment 
        self.x = self.wghtRndd - 45 #subtracts the weight of the bar             
        self.plate45 = (math.floor((self.x // 45) / 2)) * 2 #divides x by 45 and saves the integer to a variable
        self.x = self.x % 45  #divides x by 45 and replaces the original value with the remainder
        self.plate25 = (math.floor((self.x // 25) / 2)) * 2  #vvv repeats       
        if self.plate25 != 0:  # passes a remainder only when plates from this weight bracket are used
            self.x = self.x % 25
        self.plate10 = (math.floor((self.x // 10) / 2)) * 2
        if self.plate10 != 0:
            self.x = self.x % 10
        self.plate5 = (math.floor((self.x // 5) / 2)) * 2
        if self.plate5 != 0:
            self.x = self.x % 5
        self.plate2 = self.x // 2.5
        valueList= (self.plate45, self.plate25, self.plate10, self.plate5, self.plate2) #creates a tuple
        print(valueList) #test
        self.lbl1.configure(text = str(valueList[0]))  #configures the label with a text value of 
        self.lbl2.configure(text = str(valueList[1]))  #a value from the tuple converted to a string
        self.lbl3.configure(text = str(valueList[2]))
        self.lbl4.configure(text = str(valueList[3]))
        self.lbl5.configure(text = str(valueList[4]))

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid(sticky= tk.N, padx = 2, pady = 2)
    root.mainloop()
