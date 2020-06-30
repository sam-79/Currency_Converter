from tkinter import *
from tkinter import ttk

import requests
import json
import currencies

base_url="http://api.currencylayer.com/"
my_key="97a228fb88cd755a026d1b73cb650636"



def convert():
	src_key=keys[cb1.current()]
	to_key=keys[cb2.current()]
	url=base_url+"live?access_key="+my_key
	req=requests.get(url)
	data=req.json()
	rates=data["quotes"]
	src=rates["USD"+src_key]
	to=rates["USD"+to_key]	
	
	amt=float(text.get())
	f_amt=round((amt*to)/src,4)
	
	v.set(f_amt+to)




json_dict=currencies.allcurrencies()

dict=json_dict["currencies"]
keys=list(dict.keys())
list=list(dict.items())



# Main Window Design

root=Tk()
root.title('Currency Converter')
root.geometry("1000x1500")
root.minsize(1000,1500)

m=Menu(root)
op_menu=Menu(m,tearoff=0)


op_menu.add_command(label="Historial Rates")
m.add_cascade(label="Options  ",menu=op_menu)

m.add_cascade(label="help  ")
m.add_command(label="exit",command=exit)
m.config(background="#BDBDBD")
root.config(menu=m)

head=Label(root,text="Currency Converter",font=("Arial",14))
head.pack(side='top',pady=25)


lab=Label(root,text="Enter amount")
lab.pack(pady=(50,0),padx=50,anchor=W)

text=Entry(root,width=30)
text.pack(padx=50,anchor=W,fill=X)
#amt=text.get()
#print(amt)


lab1=Label(root,text="From")
lab1.pack(pady=(80,0),padx=50,anchor=W)

cb1=ttk.Combobox(root,values=list,width=30,state="readonly")
cb1.current(0)
cb1.pack(padx=50,anchor=W,fill=X) 



lab2=Label(root,text="To")
lab2.pack(pady=(80,0),padx=50,anchor=W)

cb2=ttk.Combobox(root,values=list,width=30,state="readonly")
cb2.current(0)
cb2.pack(padx=50,anchor=W,fill=X)




lab3=Label(root,text="Result")
lab3.pack(pady=(80,0),padx=50,anchor=W)

v=StringVar()
res_box=Entry(root,width=30,state="readonly",textvariable=v)
res_box.pack(padx=50,anchor=W,fill=X)
#v.set(#Rsesult Here)


Btn=Button(root,text="Calculate",command=convert) 
Btn.pack(pady=50)

exit_btn=Button(root,text="Exit",command=exit)
exit_btn.pack(pady=29)



root.mainloop()
