from tkinter import *
from tkinter import ttk

import requests
import json


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




json_dict={
  "currencies":{
    "AED":"United Arab Emirates Dirham",
    "AFN":"Afghan Afghani",
    "ALL":"Albanian Lek",
    "AMD":"Armenian Dram",
    "ANG":"Netherlands Antillean Guilder",
    "AOA":"Angolan Kwanza",
    "ARS":"Argentine Peso",
    "AUD":"Australian Dollar",
    "AWG":"Aruban Florin",
    "AZN":"Azerbaijani Manat",
    "BAM":"Bosnia-Herzegovina Convertible Mark",
    "BBD":"Barbadian Dollar",
    "BDT":"Bangladeshi Taka",
    "BGN":"Bulgarian Lev",
    "BHD":"Bahraini Dinar",
    "BIF":"Burundian Franc",
    "BMD":"Bermudan Dollar",
    "BND":"Brunei Dollar",
    "BOB":"Bolivian Boliviano",
    "BRL":"Brazilian Real",
    "BSD":"Bahamian Dollar",
    "BTC":"Bitcoin",
    "BTN":"Bhutanese Ngultrum",
    "BWP":"Botswanan Pula",
    "BYN":"New Belarusian Ruble",
    "BYR":"Belarusian Ruble",
    "BZD":"Belize Dollar",
    "CAD":"Canadian Dollar",
    "CDF":"Congolese Franc",
    "CHF":"Swiss Franc",
    "CLF":"Chilean Unit of Account (UF)",
    "CLP":"Chilean Peso",
    "CNY":"Chinese Yuan",
    "COP":"Colombian Peso",
    "CRC":"Costa Rican Col\u00f3n",
    "CUC":"Cuban Convertible Peso",
    "CUP":"Cuban Peso",
    "CVE":"Cape Verdean Escudo",
    "CZK":"Czech Republic Koruna",
    "DJF":"Djiboutian Franc",
    "DKK":"Danish Krone",
    "DOP":"Dominican Peso",
    "DZD":"Algerian Dinar",
    "EGP":"Egyptian Pound",
    "ERN":"Eritrean Nakfa",
    "ETB":"Ethiopian Birr",
    "EUR":"Euro",
    "FJD":"Fijian Dollar",
    "FKP":"Falkland Islands Pound",
    "GBP":"British Pound Sterling",
    "GEL":"Georgian Lari",
    "GGP":"Guernsey Pound",
    "GHS":"Ghanaian Cedi",
    "GIP":"Gibraltar Pound",
    "GMD":"Gambian Dalasi",
    "GNF":"Guinean Franc",
    "GTQ":"Guatemalan Quetzal",
    "GYD":"Guyanaese Dollar",
    "HKD":"Hong Kong Dollar",
    "HNL":"Honduran Lempira",
    "HRK":"Croatian Kuna",
    "HTG":"Haitian Gourde",
    "HUF":"Hungarian Forint",
    "IDR":"Indonesian Rupiah",
    "ILS":"Israeli New Sheqel",
    "IMP":"Manx pound",
    "INR":"Indian Rupee",
    "IQD":"Iraqi Dinar",
    "IRR":"Iranian Rial",
    "ISK":"Icelandic Kr\u00f3na",
    "JEP":"Jersey Pound",
    "JMD":"Jamaican Dollar",
    "JOD":"Jordanian Dinar",
    "JPY":"Japanese Yen",
    "KES":"Kenyan Shilling",
    "KGS":"Kyrgystani Som",
    "KHR":"Cambodian Riel",
    "KMF":"Comorian Franc",
    "KPW":"North Korean Won",
    "KRW":"South Korean Won",
    "KWD":"Kuwaiti Dinar",
    "KYD":"Cayman Islands Dollar",
    "KZT":"Kazakhstani Tenge",
    "LAK":"Laotian Kip",
    "LBP":"Lebanese Pound",
    "LKR":"Sri Lankan Rupee",
    "LRD":"Liberian Dollar",
    "LSL":"Lesotho Loti",
    "LTL":"Lithuanian Litas",
    "LVL":"Latvian Lats",
    "LYD":"Libyan Dinar",
    "MAD":"Moroccan Dirham",
    "MDL":"Moldovan Leu",
    "MGA":"Malagasy Ariary",
    "MKD":"Macedonian Denar",
    "MMK":"Myanma Kyat",
    "MNT":"Mongolian Tugrik",
    "MOP":"Macanese Pataca",
    "MRO":"Mauritanian Ouguiya",
    "MUR":"Mauritian Rupee",
    "MVR":"Maldivian Rufiyaa",
    "MWK":"Malawian Kwacha",
    "MXN":"Mexican Peso",
    "MYR":"Malaysian Ringgit",
    "MZN":"Mozambican Metical",
    "NAD":"Namibian Dollar",
    "NGN":"Nigerian Naira",
    "NIO":"Nicaraguan C\u00f3rdoba",
    "NOK":"Norwegian Krone",
    "NPR":"Nepalese Rupee",
    "NZD":"New Zealand Dollar",
    "OMR":"Omani Rial",
    "PAB":"Panamanian Balboa",
    "PEN":"Peruvian Nuevo Sol",
    "PGK":"Papua New Guinean Kina",
    "PHP":"Philippine Peso",
    "PKR":"Pakistani Rupee",
    "PLN":"Polish Zloty",
    "PYG":"Paraguayan Guarani",
    "QAR":"Qatari Rial",
    "RON":"Romanian Leu",
    "RSD":"Serbian Dinar",
    "RUB":"Russian Ruble",
    "RWF":"Rwandan Franc",
    "SAR":"Saudi Riyal",
    "SBD":"Solomon Islands Dollar",
    "SCR":"Seychellois Rupee",
    "SDG":"Sudanese Pound",
    "SEK":"Swedish Krona",
    "SGD":"Singapore Dollar",
    "SHP":"Saint Helena Pound",
    "SLL":"Sierra Leonean Leone",
    "SOS":"Somali Shilling",
    "SRD":"Surinamese Dollar",
    "STD":"S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra",
    "SVC":"Salvadoran Col\u00f3n",
    "SYP":"Syrian Pound",
    "SZL":"Swazi Lilangeni",
    "THB":"Thai Baht",
    "TJS":"Tajikistani Somoni",
    "TMT":"Turkmenistani Manat",
    "TND":"Tunisian Dinar",
    "TOP":"Tongan Pa\u02bbanga",
    "TRY":"Turkish Lira",
    "TTD":"Trinidad and Tobago Dollar",
    "TWD":"New Taiwan Dollar",
    "TZS":"Tanzanian Shilling",
    "UAH":"Ukrainian Hryvnia",
    "UGX":"Ugandan Shilling",
    "USD":"United States Dollar",
    "UYU":"Uruguayan Peso",
    "UZS":"Uzbekistan Som",
    "VEF":"Venezuelan Bol\u00edvar Fuerte",
    "VND":"Vietnamese Dong",
    "VUV":"Vanuatu Vatu",
    "WST":"Samoan Tala",
    "XAF":"CFA Franc BEAC",
    "XAG":"Silver (troy ounce)",
    "XAU":"Gold (troy ounce)",
    "XCD":"East Caribbean Dollar",
    "XDR":"Special Drawing Rights",
    "XOF":"CFA Franc BCEAO",
    "XPF":"CFP Franc",
    "YER":"Yemeni Rial",
    "ZAR":"South African Rand",
    "ZMK":"Zambian Kwacha (pre-2013)",
    "ZMW":"Zambian Kwacha",
    "ZWL":"Zimbabwean Dollar"
  }
}

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
