from tkinter import*
root = Tk()
root.title("dfhdjighbfvcjfb")
root.geometry("400x400")

label_series = Label(root,text="Fivba(Shortcut) Series ")
label_flower = Label(root)
label_spidel = Label(root)
label_unspidel = Label(root)

entry_no = Entry(root)

def fib():
    
    input_no = int(entry_no.get())
    first = 0
    second = 1
    sum = 0
    sum2 = 0
    counter = 1
    while(counter <= input_no):
        label_series["text"]+=str(sum)+" "
        counter = counter + 1
        first = second
        second = sum
        sum  = first + second
        sum2 = sum2 + sum

    label_flower["text"]="Flower Is Fully Blumed"
    label_unspidel["text"]="Th Monsters Preffered number is " + str(sum2)
    label_spidel["text"]="Spiden Monster in right direction are " + str(first) + " In monster preferred direction is " + str(second) + "\n total " + str(sum)

btn = Button(root,text = "Show Fivba",command = fib)
btn.pack()
label_series.pack()
label_flower.pack()
label_spidel.pack()
label_unspidel.pack()
entry_no.pack()
root.mainloop()
