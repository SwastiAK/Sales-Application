# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:53:17 2022

@author: Swasti
"""

from  tkinter import *

root = Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(background = 'pink')

label_month = Label(root)
label_profit = Label(root)

label_max_profit = Label(root)
label_min_profit = Label(root)

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000, 45983, 45620, 47103, 50000, 490000, 47653, 32100, 78600, 80000, 132650, 45698)

label_month ["text"] = "Months : " + str(month)
label_profit ["text"] = "Profits : " + str(profits)

def maxProfit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit["text"] = "The Maximum Profit Of " + str(max_profit) + " Was Recorded In The Month Of " + str(max_profit_month)
    
def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = month[min_profit_index]
    label_min_profit ["text"] = "The Minimum Profit Of " + str(min_profit) + " Was Recorded In The Month Of " + str(min_profit_month)
    
label_month.place(relx = 0.5, rely = 0.2, anchor = CENTER)
label_profit.place(relx = 0.5, rely = 0.3, anchor = CENTER)

btn_max = Button(root, text = "Show Max Profitable Month", command = maxProfit, bg="blue")
btn_min = Button(root, text = "Show Min Profitable Month", command = minProfit, bg="blue")

btn_max.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_max_profit.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn_min.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_min_profit.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()