#did it ALLL by myself!
from tkinter import *

window=Tk()
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)


textbox=Entry(width=20)
textbox.grid(column=2, row=0)
textbox.insert(END,string="0")

miles_label=Label(text="Miles")
miles_label.grid(column=3,row=0)
miles_label.config(padx=10,pady=5)

is_equal=Label(text="is equal to")
is_equal.grid(column=1,row=1)
is_equal.config(padx=3,pady=10)

ans_km=Label(text="0")
ans_km.grid(column=2,row=1 )
ans_km.config(padx=20,pady=30)

def conversion():
    miles=int(textbox.get())
    result=miles*1.6
    return ans_km.config(text=result)

calculate_button=Button(text="Calculate", command=conversion)
calculate_button.grid(column=2,row=2)

km_label=Label(text="Km")
km_label.grid(column=3, row=1)


window.mainloop()
