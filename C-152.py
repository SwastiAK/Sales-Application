# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:17:28 2022

@author: Swasti
"""

from tkinter import*
root = Tk()
root.title("Multidimentional Arrays")

root.geometry("400x400")
label = Label(root)

array_1d = ["Ishvari", "Shreya", "Rajlaxmi"]
print(array_1d[0])

array_2d = [["Ishvari","A+"],["Shreya", "A"],["Rajlaxmi","B"]]
print(array_2d[0][1])

array_3d = [[["Ishavri","A+","Excellent"],["Shreya","A","Very Good"],["Rajlaxmi","B","Good"]]]
print(array_3d[0][0][2])

def report():
    label ["text"] = array_3d[0][1][0] + " Got Grade " + array_3d[0][1][1] + " As She Is Doing " + array_3d[0][1][2]
    
btn = Button(root, text = "Show Report", command = report)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()