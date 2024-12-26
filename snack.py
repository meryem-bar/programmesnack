from tkinter import *

def cal_tot():
    tot = 0
    
    for i, quan in enumerate(quantites_vars):
        qan = int(quan.get())  
        pr = float(prixx[i]) 
        tot += qan * pr 
        

    total_label.config(text=f"Total: {tot:.2f} DH")  



fa = Tk()
fa.geometry('800x700')
fa.title('Snack de Fatima et Meryem')

frl = Frame(fa, width=690, height=499, background='gray')
frl.place(x=1, y=1)

fr2 = Frame(fa, width=690, height=499, bg='pink')
fr2.place(x=693, y=1)

Label(frl, text="Bienvenue! à notre premier snack.Si vous voulez quelque chose, dites-le-nous simplement dans le commentaire.Dites-nous si la nourriture était bonne ou mauvaise.Merci pour votre visite."
, bg='gray', wraplength=350, cursor='heart', font=('Georgia', 18, 'bold'), justify='left').place(x=10, y=12)

paiement_var = StringVar(value="Espèces")
Label(frl, text="Mode de paiement :", bg='gray', cursor='heart', font=('Georgia', 12, 'bold')).place(x=20, y=300)

Radiobutton(frl, text="Cash", variable=paiement_var, cursor='heart', value="Espèces", bg='gray', font=('Georgia', 12)).place(x=20, y=330)
Radiobutton(frl, text="Carte bancaire", variable=paiement_var, cursor='heart', value="Carte bancaire", bg='gray', font=('Georgia', 12)).place(x=220, y=330)
Radiobutton(frl, text="Mobile", cursor='heart', variable=paiement_var, value="Mobile", bg='gray', font=('Georgia', 12)).place(x=370, y=330)

commentaire_var = StringVar()
Label(frl, text="Commentaire :", bg='gray', cursor='heart', font=('Georgia', 12, 'bold')).place(x=5, y=370)
Entry(frl, textvariable=commentaire_var, cursor='heart', width=30, font=('Georgia', 12)).place(x=5, y=400)

menu = [
    "Pizza",
    "Tacos",
    "Sandwich",
    "Burger",
    "Frites",
    "Nuggets",
    "Soda",
    "Limonade"
]

prixx = [
    40.00,
    49.00,
    30.00,
    32.00,
    15.00,
    35.00,
    15.00,
    18.00
]


quantites_vars = []
y_position = 10

for item, price in zip(menu, prixx):
    Label(fr2, text=f"{item} ({price:.2f} DH)", bg='pink', cursor='heart', font=('Georgia', 12)).place(x=10, y=y_position)
    quan = StringVar()
    quantites_vars.append(quan)
    Entry(fr2, textvariable=quan, width=5, cursor='heart', font=('Georgia', 12)).place(x=250, y=y_position)
    y_position =y_position + 40

total_label = Label(fr2, text="Total: 0.00 DH", cursor='heart', bg='pink', font=('Georgia', 14, 'bold'))
total_label.place(x=10, y=330)


bt2 = Button(fr2, text='Calculer Total', fg='white', width=30, bg='black', cursor='heart', font=('Georgia', 12, 'bold'), command=cal_tot)
bt2.place(x=10, y=400)

men = Menu(fa)

nav = Menu(men, cursor='heart')
nav.add_command(label='Emporter')
nav.add_separator()
nav.add_command(label='Snack')
nav.add_separator()
nav.add_command(label='Fin Commande', command=fa.quit)

men.add_cascade(label='Click Click', menu=nav)
fa.config(menu=men)

fa.mainloop()