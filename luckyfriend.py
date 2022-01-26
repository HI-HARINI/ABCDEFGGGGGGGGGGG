from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("Lucky Friend-1D")

label1=Label(root)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(list1)

def rn():
    length=len(list1)
    ranu1=random.randint(0, length)
    ranu2=random.randint(0, length)
    ranu3=random.randint(0, length)
    ranu4=random.randint(0, length)
    ranu5=random.randint(0, length)
    random1=list1[ranu1]
    random2=list1[ranu2]
    random3=list1[ranu3]
    random4=list1[ranu4]
    random5=list1[ranu5]

    label1["text"]=random1+random2+random3+random4+random5

button=Button(root,text="RANDOM WORDSSSS!!!!!",command=rn)
button.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()