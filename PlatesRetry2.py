import tkinter as tk
from tkinter import Tk



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
        self.btn1 = tk.Button(parent, text = "Calculate", bg = "red", fg = "black", command =lambda: Clicks.clicked, font = ("Arial", 20))
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
        self.lbl1 = tk.Label(parent, text = Clicks.clicked.valueList[0], bg ="red", font = ("Arial Bold", 20))
        self.lbl1.grid(column = 1, row = 6, sticky = tk.W)
        self.lbl2 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl2.grid(column = 1, row = 7, sticky = tk.W)
        self.lbl3 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl3.grid(column = 1, row = 8, sticky = tk.W)
        self.lbl4 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl4.grid(column = 1, row = 9, sticky = tk.W)
        self.lbl5 = tk.Label(parent, bg ="red", font = ("Arial Bold", 20))
        self.lbl5.grid(column = 1, row = 10, sticky = tk.W) 

class Clicks:
    def __init__(self, parent, Var, *args, **kwargs):
        tk.Frame.__init__(self, parent, Var, *args, **kwargs)
    # handles the button click event
    def clicked(self, parent):
        out = parent.entry.get()#saves value in entry box to a variable
        int_out = int(out)#converts that to an integer and saves to a new variable
        #calculations
        P = Plates(int_out)#call Plates as p
        valueList = P.calculate(P.consolidate(P.myround(int_out)))
        #^^^rounds the input to the nearest 5lb, subtracts 45, returns the number of each plate as a tuple
        #assigns that tuple to the variable valueList
        parent.lbl1.configure(text = valueList[0])
        parent.lbl2.configure(text = valueList[1])
        parent.lbl3.configure(text = valueList[2])
        parent.lbl4.configure(text = valueList[3])
        parent.lbl5.configure(text = valueList[4])
        return valueList
         

class Plates:
   
    def __init__(self, totalWeight):
        '''assigns the total weight and weight of the barbell'''
        self.totalWeight = totalWeight

    def myround(self, z):
        '''Rounds to the nearest 5lb increment'''
        return 5 * round(z/5)
    
    def consolidate(self, totalWeight):
        '''Takes the arguments totalWeight and barWeight, rounds them, then calculates the weight
        we're solving for by subracting barWeight from totalWeight'''
        self.wghtRndd = self.myround(self.totalWeight)
        self.weight = self.wghtRndd - 45

    def calculate(self, x):
        '''divides the weight by the plate weight to get the number of plates'''
        #simplifying the calculation
        self.x = x              
        self.plate45 = self.x // 45
        self.x = self.x % 45
        self.plate25 = self.x // 25
        self.x = self.x % 25
        self.plate10 = self.x // 10
        self.x = self.x % 10
        self.plate5 = self.x // 5
        self.x = self.x % 5
        self.plate2 = self.x // 2.5
        print(self.plate45, self.plate25, self.plate10, self.plate5, self.plate2)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid(sticky= tk.N, padx = 2, pady = 2)
    root.mainloop()
