from tkinter import *
from tkinter import ttk

form = Tk()

getFld = IntVar()

f = open("data.txt", "r")
total = f.read()
f.close()

form.wm_title('Ödeme')

stepOne = LabelFrame(form, text=" 1. Kişisel Bilgiler: ")
stepOne.grid(row=0, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

helpLf = LabelFrame(form, text="Toplam Fiyat")
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
            sticky='NS', padx=5, pady=5)
helpLbl = Label(helpLf, text=total)
helpLbl.grid(row=0)


satınal_butonu = Button(helpLf, text="Satın Al")
satınal_butonu.grid(row=0, column=3)

stepTwo = LabelFrame(form, text=" 2. Kredi Kartı Bilgileri: ")
stepTwo.grid(row=2, columnspan=7, sticky='W', \
             padx=5, pady=5, ipadx=5, ipady=5)

stepThree = LabelFrame(form, text=" 3. Kullanıcı Sözleşmesi: ")
stepThree.grid(row=3, columnspan=7, sticky='W', \
               padx=5, pady=5, ipadx=5, ipady=5)

name_label = Label(stepOne, text="İsim")
name_label.grid(row=0, column=0, sticky='E', padx=5, pady=2)

name_entry = Entry(stepOne)
name_entry.grid(row=0, column=1, sticky="WE", pady=3)


lastname_label = Label(stepOne, text="Soyisim")
lastname_label.grid(row=0, column=2, sticky='E', padx=5, pady=2)

lastname_entry = Entry(stepOne)
lastname_entry.grid(row=0, column=3, sticky="WE", pady=3)

email_label= Label(stepOne, text="Elektronik Posta")
email_label.grid(row=0, column=4, sticky='E', padx=5, pady=2)

email_entry = Entry(stepOne)
email_entry.grid(row=0, column=5, sticky="WE", pady=3, columnspan=3)

adres_label = Label(stepOne, text="Adres")
adres_label.grid(row=1, column=0, sticky='E', padx=5, pady=2)

adres_entry = Entry(stepOne)
adres_entry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

postakodu_label = Label(stepOne, text="Posta Kodu")
postakodu_label.grid(row=2, column=0, sticky='E', padx=5, pady=2)

postakodu_entry = Entry(stepOne)
postakodu_entry.grid(row=2, column=1, sticky='E', pady=2)

tel_label = Label(stepOne, text="Telefon Numarası")
tel_label.grid(row=2, column=2, padx=5, pady=2)

tel_entry = Entry(stepOne)
tel_entry.grid(row=2, column=3, pady=2)

kartisim_label = Label(stepTwo, \
                      text="Kart Üzerindeki İsim:")
kartisim_label.grid(row=3, column=0, sticky='W', padx=5, pady=2)

kartisim_entry = Entry(stepTwo)
kartisim_entry.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')

kartnum_label = Label(stepTwo, \
                      text="Kart Numarası:")
kartnum_label.grid(row=4, column=0, sticky='W', padx=5, pady=2)

kartnum_entry = Entry(stepTwo)
kartnum_entry.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')

skk_label = Label(stepTwo, text="Son Kullanma Tarihi:")
skk_label.grid(row=5, column=0, padx=5, pady=2, sticky='W')

skk_entry = Entry(stepTwo)
skk_entry.grid(row=5, column=1,padx=5, pady=2, sticky='WE')

cvv_label = Label(stepTwo, text="CVV:")
cvv_label.grid(row=5, column=2, padx=5, pady=2, sticky='W')

cvv_entry = Entry(stepTwo)
cvv_entry.grid(row=5, column=3,padx=5, pady=2, sticky='WE')

transChk = Checkbutton(stepThree, \
           text="Uzaktan Satış Sözleşmesini okudum", onvalue=1, offvalue=0)
transChk.grid(row=6, sticky='W', padx=5, pady=2)







form.mainloop()






