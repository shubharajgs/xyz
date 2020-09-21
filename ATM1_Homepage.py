from tkinter import *
window = Tk()

window.state("zoomed")
window.configure(bg="lightskyblue")
window.title("Canara Bank")

#method to entering into next page when we hit enter

def go():
    window.destroy()
    import ATM2_First_page
    
    
    

#to create an heading in home page
Label1= Label(window, text="WELCOME",font=("helvetica",60) ,height=3,width=33,fg="yellow2")
Label1.place(x=2,y=200)

Label2= Label(window, text="to Canara Bank",font=("helvetica",30) ,height=2,width=80,fg="grey2")
Label2.place(x=4,y=375)


#inserting card option
Label3= Button(window, text="Please insert your card",font=("helvetica",25) ,height=2,width=81,bg="lightskyblue",command = go)
Label3.place(x=0,y=600)

window.after(2000,go)#2000 means 2000nanoseconds it lasts for 2 sec..then next screen appears



window.mainloop()


