# Parikh, Parshva
# 2020/09/22
# ICS4U1-01
# Tip Calculator
# Features: "Help" button, "Quit" button and the program accounts for a 5% sales tax

from tkinter import *       #import tkinter modules to use it widgets and the corresponding widgets, properties, etc.
from tkinter import messagebox

def show_help():    #display help message with a button click to assist user
    messagebox.showinfo("Info", "This program will calculate a total bill including tip percentage and the amount of "
                                "money per person. The program will only accept numerical values, so inputting "
                                "a '$'/'%' symbol, words or a blank will result in a error report and a request to "
                                "re-prompt. \n\n"
                                "Note: Total bill and tip percentage cannot be lower than 0 and the number of people "
                                "cannot be lower than 1 (errors will be reported).\n\n"
                                "Note: Tip is calculated pre-tax.")

def ask_exit():     #confirm that user wants to exit if user clicks the window X or the exit button
    answer = messagebox.askyesno('Exit', 'Do you want to exit?')
    if answer:      #if user clicks yes then close the window
        exit()

def clear_txt():        #when user clicks clear, wipe the text from the entry widgets
    btnOk.config(state = 'active')

    txtBill.delete(0, END)      #clear the input widgets and set it to the minimum amount
    txtBill.insert(0, '0')
    txtBill.focus()
    txtBill.selection_range(0, END)
    txtPeople.delete(0, END)
    txtPeople.insert(0, '1')
    txtTipP.delete(0, END)
    txtTipP.insert(0, '0')

    x = [txtTipA, txtGAmount, txtTotalPer]      #create list for the last 3 entry boxes
    for a in x:                                 #clear the widget with a loop so the code doesn't repeat
        a.config(state = 'normal')
        a.delete(0, END)
        a.config(state = 'readonly')

def check_val():            #when user presses ok, proceed to error check all the inputted values
    try:
        bill = float(txtBill.get())     #convert entry value from string to float
        if bill < 0:                    #if the bill is < $0, then display message explaining error
            messagebox.showerror('Invalid Data', 'The bill amount cannot be < 0.')
            red_bg(txtBill)         #highlight the entry box of the error
            pass                    #return back to user input phase
        else:               #if input is valid continue checking the other inputs
            try:
                people = int(txtPeople.get())
                if people < 1:
                    messagebox.showerror('Invalid Data', 'You cannot have < 1 person.')
                    red_bg(txtPeople)
                    pass
                else:
                    try:
                        tip = float(txtTipP.get())
                        if tip < 0:
                            messagebox.showerror('Invalid Data', 'The tip % cannot be 0.')
                            red_bg(txtTipP)
                            pass
                        else:
                            calc_val(bill, people, tip)   #if all inputs are valid, then pass the values for calculation
                    except:
                        messagebox.showerror('Invalid Data',
                                             "Please fill in the required fields with valid data. See 'Help' for more.")
                        red_bg(txtTipP)     #if a blank or a different value input is given, report error and highlight
            except:
                messagebox.showerror('Invalid Data',
                                     "Please fill in the required fields with valid data. See 'Help' for more.")
                red_bg(txtPeople)
    except:
        messagebox.showerror('Invalid Data', "Please fill in the required fields with valid data. See 'Help' for more.")
        red_bg(txtBill)

def calc_val(bill, people, tip):
    tax = 1.05      #set tax percentage to variable for calculation

    tip = bill * (tip / 100)        #convert tip percent to decimal and multiple by bill for tip price
    total = (bill + tip) * tax      #the sum of the tip and the bill multiplied by 1.05(tax) is the total price
    totalper = total / people       #the amount of money each person should pay

    insert_val(round(tip, 2), txtTipA)   #round the prices to the 2nd decimal and pass them to a function for displaying
    insert_val(round(total, 2), txtGAmount)
    insert_val(round(totalper, 2), txtTotalPer)

def insert_val(value, widget):      #open the readonly widgets, insert the calculated values and return to readonly
    widget.config(state = 'normal')
    widget.insert(0, '$' + str(value))
    widget.config(state = 'readonly')
    #disable the ok button so the values don't add themselves again (runtime error)
    btnOk.config(state = 'disabled')

def red_bg(widget):     #highlight the widget holding the error red and then change it to white when user clicks it
    widget.config(background="red")
    widget.focus()
    widget.selection_range(0, END)
    widget.bind("<Key>", lambda event: reset_widget(widget))

def reset_widget(widget):       #change a widget's background to white when user clicks it
    widget.config(background="white")

root = Tk()     #create window, set title and set the window exit option to display a prompt
root.title('Tip Calculator')
root.protocol('WM_DELETE_WINDOW', ask_exit)

fr = Frame(root, padx = 10, pady = 10)      #set frame and add it window
fr.pack()

title = PhotoImage(file = 'title_logo.png')     #set images for logo and the title to variables
symbol = PhotoImage(file = 'tip_calculator.png')        #put the images in a label to display
lblTitle = Label(fr, image = title).grid(row = 0, column = 0, columnspan = 4, pady = 5)
lblSymbol = Label(fr, image = symbol).grid(row = 1, column = 0, padx = 10, pady = 5, rowspan = 9, columnspan = 2)

#create labels to prompt user what to input in the entry boxes and set and organize them on the frame's grid
lblBill = Label(fr, text = 'Bill: ', font = ('TkDefaultFont', 12, 'bold'),
                fg = 'SlateGray4').grid(row = 1, column = 2, sticky = 'w', pady = 10, padx = 5)
lblPeople = Label(fr, text = 'Total people: ', font = ('TkDefaultFont', 12, 'bold'),
                  fg = 'SlateGray4').grid(row = 2, column = 2, sticky = 'w', pady = 10, padx = 5)
lblPercent = Label(fr, text = 'Tip percentage: ', font = ('TkDefaultFont', 12, 'bold'),
                   fg = 'SlateGray4').grid(row = 3, column = 2, sticky = 'w', pady = 10, padx = 5)
lblTax = Label(fr, text = 'Tax percentage: ', font = ('TkDefaultFont', 12, 'bold'),
               fg = 'SlateGray4').grid(row = 4, column = 2, sticky = 'w', pady = 10, padx = 5)
lblTip = Label(fr, text = 'TIP AMOUNT: ', font = ('TkDefaultFont', 12, 'bold'),
               fg = 'SlateGray4').grid(row = 6, column = 2, sticky = 'w', pady = 10, padx = 5)
lblTotal = Label(fr, text = 'GRAND AMOUNT: ', font = ('TkDefaultFont', 12, 'bold'),
                 fg = 'SlateGray4').grid(row = 7, column = 2, sticky = 'w', pady = 10, padx = 5)
lblTP = Label(fr, text = 'TOTAL/PERSON: ', font = ('TkDefaultFont', 12, 'bold'),
              fg = 'SlateGray4').grid(row = 8, column = 2, sticky = 'w', pady = 10, padx = 5)

#create buttons and organize them on the grid
#set commands for calculations/checking values, displaying info, clearing info and ending the program
btnOk = Button(fr, text = 'OK', font = ('TkDefaultFont', 12, 'bold'), width = 12, fg = 'SlateGray4',
               relief = 'raised', command = check_val)
btnOk.grid(row = 5, column = 2, pady = 10, ipadx = 5, padx = 5)
btnClear = Button(fr, text = 'CLEAR', font = ('TkDefaultFont', 12, 'bold'), width = 12, fg = 'SlateGray4',
                  relief = 'raised', command = clear_txt).grid(row = 5, column = 3, pady = 10, ipadx = 5, padx = 5)
btnHelp = Button(fr, text = 'HELP', font = ('TkDefaultFont', 12, 'bold'), width = 12, fg = 'SlateGray4',
                 relief = 'raised', command = show_help).grid(row = 9, column = 2, pady = 10, ipadx = 5, padx = 5)
btnQuit = Button(fr, text = 'EXIT', font = ('TkDefaultFont', 12, 'bold'), width = 12, fg = 'SlateGray4',
                 relief = 'raised', command = ask_exit).grid(row = 9, column = 3, pady = 10, ipadx = 5, padx = 5)

#create entry boxes and organize them on grid, 3 for user input
txtBill = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), bg = 'white')
txtBill.grid(row = 1, column = 3,
             pady = 10, padx = 10)
txtPeople = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), bg = 'white')
txtPeople.grid(row = 2, column = 3,
               pady = 10, padx = 10)
txtTipP = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), bg = 'white')
txtTipP.grid(row = 3, column = 3,
             pady = 10, padx = 10)

#create entry boxes that display info that's been calculated from the user input and set them on the grid
#set to readonly so user can't change the values being output
txtTax = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12,), readonlybackground = 'white')
txtTax.grid(row = 4, column = 3,
            pady = 10, padx = 10)
txtTax.insert(0, '5%')      #insert constant tax value and set to readonly
txtTax.config(state = 'readonly')
txtTipA = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), readonlybackground = 'white',
                state = 'readonly')
txtTipA.grid(row = 6, column = 3,
             pady = 10, padx = 10)
txtGAmount = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), readonlybackground = 'white',
                   state = 'readonly')
txtGAmount.grid(row = 7, column = 3,
                pady = 10, padx = 10)
txtTotalPer = Entry(fr, justify = 'center', font = ('TkDefaultFont', 12), readonlybackground = 'white',
                    state = 'readonly')
txtTotalPer.grid(row = 8, column = 3,
                 pady = 10, padx = 10)

root.mainloop()         #loop the window so it can be used as many times as necessary before user selects exit
