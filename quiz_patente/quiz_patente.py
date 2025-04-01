import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
import domande
from random import *
import time

class Home(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title('Quiz patente B')
        self.master.geometry('1920x1080')
        self.grid()
        self.crea_widgets()

    def crea_widgets(self):

        bg = tk.Label(self.master, bg="#cfe6d6", width=1920, height=1080, borderwidth=1)
        bg.place(x=0, y=0)  

        label_title = tk.Label(self.master, text="QUIZ PATENTE B", font=("Arial", 40, "bold"), bg="#cfe6d6", fg='green')
        label_title.place(relx=0.5, rely=0.1, anchor="center")


        self.master.label_img = tk.Label(self.master)
        self.master.label_img.place(relx = 0.5, rely = 0.37, anchor='s') 
        self.master.img_tk = tk.PhotoImage(file='./assets/img_iniziale.png')        
        self.master.label_img.config(image=self.master.img_tk, highlightbackground = "green", highlightcolor= "green", highlightthickness=2) 
        

        label_esercitazione1 = tk.Label(self.master, text="ESERCITAZIONE 1", font=("Arial", 10), bg="#cfe6d6").place(relx=0.2, rely=0.43, anchor="center")
        start_btn = tk.Button(self.master, text="Segnali di pericolo", font=("Arial", 13, "bold"), bg="lightgreen",fg="black", command= lambda: main_esercitazioni('segnali di pericolo'))        
        start_btn.place(relx=0.2, rely=0.5, anchor="center")
        start_btn.config(width=35, height=5)

        label_esercitazione2 = tk.Label(self.master, text="ESERCITAZIONE 2", font=("Arial", 10), bg="#cfe6d6").place(relx=0.5, rely=0.43, anchor="center")
        start_btn = tk.Button(self.master, text="Le precedenze", font=("Arial", 13, "bold"),bg="lightgreen",fg="black", command= lambda: main_esercitazioni('precedenza'))        
        start_btn.place(relx=0.5, rely=0.5, anchor="center")
        start_btn.config(width=35, height=5)

        label_esercitazione3 = tk.Label(self.master, text="ESERCITAZIONE 3", font=("Arial", 10), bg="#cfe6d6").place(relx=0.8, rely=0.43, anchor="center")
        start_btn = tk.Button(self.master, text="Segnali di indicazione", font=("Arial", 13, "bold"),bg="lightgreen",fg="black", command= lambda: main_esercitazioni('indicazione'))        
        start_btn.place(relx=0.8, rely=0.5, anchor="center")
        start_btn.config(width=35, height=5)

        label_quiz = tk.Label(self.master, text="ESAME PATENTE B", font=("Arial", 10), bg="#cfe6d6").place(relx=0.5, rely=0.63, anchor="center")
        start_btn = tk.Button(self.master, text="Inizia il test", font=("Arial", 13, "bold"),bg="lightgreen",fg="black", command= main_scheda)        
        start_btn.place(relx=0.5, rely=0.7, anchor="center")
        start_btn.config(width=35, height=5)

        exit_btn = tk.Button(self.master, text='Chiudi il programma', bg="lightgreen", command= self.master.quit)
        exit_btn.place(x = 100, y= 890)
        

        
class Quiz(tk.Toplevel):    
    def __init__(self):
        super().__init__()
        self.title('Scheda 1')
        self.geometry('1920x1080')
        self.grid()
        self.N = 30
        self.i = 0
        self.punteggio = 0
        self.minuti = 30
        self.secondi = self.minuti * 60
        self.var_risposta = [tk.IntVar(value=0) for _ in range(self.N)]
        self.count = 0
        self.cons = False
        
        self.crea_widgets()

    def crea_widgets(self): 

        #sfondo + intestazione 
        bg = tk.Label(self, bg="#cfe6d6", width=1920, height=1080, relief="ridge", borderwidth=1)
        bg.place(x=0, y=0)      

        nav = tk.Label(self, bg="#32a852", width=400, height=15, relief="ridge", borderwidth=1)
        nav.place(x=0, y=0) 

        #creazione pulsanti domande
        self.btns = []
        for i in range(self.N):
            self.btn_n_domanda = tk.Button(self, text=f'{i + 1}', command=lambda i = i : self.vai_alla_domanda(i))
            self.btn_n_domanda.place(x = i*35 + 430 , y = 200)
            self.btns.append(self.btn_n_domanda)

        #label + avvia timer
        self.label_timer_txt = tk.Label(self, text='Tempo a disposizione:', bg='#cfe6d6', font=("Arial", 15))
        self.label_timer_txt.place(x = 360, y = 755)
        self.label_timer = tk.Label(self, text='00:00', bg='#cfe6d6', font=("Arial", 30, "bold"))
        self.label_timer.place(x = 400, y = 800)
        self.start_timer()

        #titolo scheda
        label_title = tk.Label(self, text="Scheda esame", font=("Arial", 20, "bold"), bg="#32a852")
        label_title.place(x = 870 , y = 50)

        #label numero domande
        self.label_n_domande = tk.Label(self, text=f"Domande:\n{self.i +1} / {self.N}", font=("Arial", 15), bg="#32a852")
        self.label_n_domande.place(x = 918, y = 130)    

        #genera domande
        self.d = []
        self.addedD = []

        while self.count < self.N:
            n_domanda = randrange(0, len(domande.domande) - 1)

            if n_domanda not in self.addedD:
                self.addedD.append(n_domanda)
                print(f"DOMANDA: {n_domanda}")
                print(f"LIST: {self.addedD}")

                self.d.append((domande.domande[n_domanda]['argomento'], 
                                domande.domande[n_domanda]['domanda'], 
                                domande.domande[n_domanda]['risposta'], 
                                domande.domande[n_domanda]['immagine']))
                self.count += 1
            else:
                print("domanda presente")

            print(domande.domande[n_domanda]['domanda'])

        print('-----')

        #label domande e immagine + chiama funzione per generare immagini
        self.label_domande = tk.Label(self, text=self.d[self.i][1], bg='#cfe6d6', font=('Arial', 15), wraplength="1000", justify="left")
        self.label_domande.place(x =750, y = 450)   

        self.label_img = tk.Label(self)
        self.label_img.place(x = 340, y = 450)
        self.carica_immagine() 
        
        #creazione checkbtn vero e falso + btn avanti e indietro e consegna
        self.chk_vero = tk.Checkbutton(self, text='V', variable=self.var_risposta[self.i], onvalue=1, offvalue=0, bg='#32a852', font=("Arial", 18), width=7, height=2, indicatoron=False)
        self.chk_vero.place(x = 1000, y= 700)

        self.chk_falso = tk.Checkbutton(self, text='F', variable=self.var_risposta[self.i], onvalue=2, offvalue=0, bg='#32a852', font=("Arial", 20), width=7, height=2, indicatoron=False)
        self.chk_falso.place(x = 1300, y= 700)

        btn_avanti = tk.Button(self, text='avanti >', bg="lightgreen",command= lambda: self.avanti())
        btn_avanti.place(x = 1750, y= 850)
        
        btn_indietro=tk.Button(self, text='< indietro', bg="lightgreen",command=lambda: self.indietro())
        btn_indietro.place(x = 1650, y= 850)

        btn_consegna = tk.Button(self, text='consegna test', bg="lightgreen",command= self.consegna)
        btn_consegna.place(x = 1000, y= 850)
        

    #metodo per avviare il timer
    def start_timer(self):
        if self.secondi > 0:
            self.min_restanti = self.secondi // 60
            self.sec_restanti = self.secondi % 60
            self.label_timer.config(text=f'{self.min_restanti:02d}:{self.sec_restanti:02d}')
            self.secondi -= 1
            self.after(1000, self.start_timer)
        else:
            messagebox.showinfo("TEMPO SCADUTO", "test consegnato")
            self.cons = True
            self.consegna()  #consegna automaticamente allo scadere del timer

    #metodo per saltare alla domanda scelta
    def vai_alla_domanda(self, indice):
        self.i = indice   
        self.label_domande.config(text=self.d[self.i][1])
        self.label_n_domande.config(text= f"Domande:\n{self.i + 1} / {self.N}")
        self.carica_immagine()

        self.chk_vero.config(variable=self.var_risposta[self.i])
        self.chk_falso.config(variable=self.var_risposta[self.i])

        print(self.i)

    #metodo per caricare l'immagine
    def carica_immagine(self):
        try:
            immagine = self.d[self.i][3]   
            self.img_tk = tk.PhotoImage(file=immagine)
            self.label_img.config(image=self.img_tk, text='') 
        except:
            self.label_img.config(image='', text='Errore durante il caricamento dell\'immagine')
    
    def consegna(self):
        self.check = False
        self.sbagliate = []
        for i in range(len(self.d)):
            if self.var_risposta[i].get() == 1 and self.d[i][2] == 'vero' or self.var_risposta[i].get() == 2 and self.d[i][2] == 'falso':
                self.punteggio += 1
            else:
                self.sbagliate.append(self.d[i][2])

        for j in range(self.N):
            if self.var_risposta[j].get() == 0:
                self.check = True
                break

        if self.cons == False:

            risposta = messagebox.askokcancel(title='consegna test', message=f'Vuoi consegnare il test?\n hai risposto a tutte le domande' if self.check == False else f'Sicuro di voler consegnare il test?\n non hai risposto a tutte le domande' )

            if risposta:
                messagebox.showinfo("TEST COMPLETATO",
                                    f'Hai superato il test:\n\nrisposte corrette: {self.punteggio}' if self.punteggio >= 27 else f'Non hai superato il test:\nrisposte giuste:{self.punteggio}')  
                self.destroy()            

        else:
            messagebox.showinfo("TEST COMPLETATO",
                                    f'Hai superato il test:\n\nrisposte corrette: {self.punteggio}' if self.punteggio >= 27 else f'Non hai superato il test:\nrisposte giuste:{self.punteggio}')             
  
            self.destroy() 

        print(self.sbagliate)


    def avanti(self): 
        if self.i < self.N:
            self.i+= 1   
            self.label_domande.config(text=self.d[self.i][1])
            self.label_n_domande.config(text= f"Domande:\n{self.i+1} / {self.N}")
            self.carica_immagine()

            self.chk_vero.config(variable=self.var_risposta[self.i])
            self.chk_falso.config(variable=self.var_risposta[self.i])

            # print(self.d[self.i][1])
            print(self.i)
        else: 
            messagebox.showerror("DOMANDE TERMINATE",
                                    "consegna il test o ricontrolla le domande")        

    def indietro(self): 
        if self.i > 0: 
            self.i-= 1   
            self.label_domande.config(text=self.d[self.i][1])
            self.label_n_domande.config(text= f"Domande:\n{self.i+1} / {self.N}")
            self.carica_immagine()

            self.chk_vero.config(variable=self.var_risposta[self.i])
            self.chk_falso.config(variable=self.var_risposta[self.i])

            # print(self.d[self.i][1])
        else:
            messagebox.showerror("impossibile tornare indietro",
                                    "sei già alla prima domanda")
        print(self.i)
            
    
class Esercitazioni(tk.Toplevel):
    def __init__(self, argomento):
        super().__init__()
        self.title('Scheda esercitazione')
        self.geometry('1920x1080')
        self.grid()
        self.N = 30
        self.argomento = argomento
        self.i = 0
        self.punteggio = 0
        self.minuti = 30
        self.secondi = self.minuti * 60
        self.var_risposta = [tk.IntVar(value=0) for _ in range(self.N)]
        self.count = 0
        self.cons = False
        self.crea_widgets()

    def crea_widgets(self): 

        #sfondo + intestazione 
        bg = tk.Label(self, bg="#cfe6d6", width=1920, height=1080, relief="ridge", borderwidth=1)
        bg.place(x=0, y=0)      

        nav = tk.Label(self, bg="#32a852", width=400, height=15, relief="ridge", borderwidth=1)
        nav.place(x=0, y=0) 

        #creazione pulsanti domande
        self.btns = []
        for i in range(self.N):
            self.btn_n_domanda = tk.Button(self, text=f'{i + 1}', command=lambda i = i : self.vai_alla_domanda(i))
            self.btn_n_domanda.place(x = i*35 + 430 , y = 200)
            self.btns.append(self.btn_n_domanda)

        #label + avvia timer
        self.label_timer_txt = tk.Label(self, text='Tempo a disposizione:', bg='#cfe6d6', font=("Arial", 15))
        self.label_timer_txt.place(x = 360, y = 755)
        self.label_timer = tk.Label(self, text='00:00', bg='#cfe6d6', font=("Arial", 30, "bold"))
        self.label_timer.place(x = 400, y = 800)
        self.start_timer()

        #titolo scheda
        label_title = tk.Label(self, text="Scheda esercitazione", font=("Arial", 20, "bold"), bg="#32a852")
        label_title.place(x = 835 , y = 50)

        #label numero domande, "bold"
        self.label_n_domande = tk.Label(self, text=f"Domande:\n{self.i +1} / {self.N}", font=("Arial", 15), bg="#32a852")
        self.label_n_domande.place(x = 925, y = 130)    

        #genera domande
        self.d = []
        self.addedD = []        

        while self.count < self.N:
            n_domanda = randrange(0, len(domande.domande) - 1)

            if n_domanda not in self.addedD and domande.domande[n_domanda]['argomento'] == self.argomento:
                self.addedD.append(n_domanda)
                print(f"DOMANDA: {n_domanda}")
                print(f"LIST: {self.addedD}")

                self.d.append((domande.domande[n_domanda]['argomento'], 
                                domande.domande[n_domanda]['domanda'], 
                                domande.domande[n_domanda]['risposta'], 
                                domande.domande[n_domanda]['immagine']))
                self.count += 1
            else:
                print("domanda presente")

            print(domande.domande[n_domanda]['domanda'])

        print('-----')

        #label domande e immagine + chiama funzione per generare immagini
        self.label_domande = tk.Label(self, text=self.d[self.i][1], bg='#cfe6d6', font=('Arial', 15), wraplength="1000", justify="left")
        self.label_domande.place(x =750, y = 450)   

        self.label_img = tk.Label(self)
        self.label_img.place(x = 340, y = 450)
        self.carica_immagine() 
        
        #creazione checkbtn vero e falso + btn avanti e indietro e consegna
        self.chk_vero = tk.Checkbutton(self, text='V', variable=self.var_risposta[self.i], onvalue=1, offvalue=0, bg='#32a852', font=("Arial", 18), width=7, height=2, indicatoron=False)
        self.chk_vero.place(x = 1000, y= 700)

        self.chk_falso = tk.Checkbutton(self, text='F', variable=self.var_risposta[self.i], onvalue=2, offvalue=0, bg='#32a852', font=("Arial", 20), width=7, height=2, indicatoron=False)
        self.chk_falso.place(x = 1300, y= 700)

        btn_avanti = tk.Button(self, text='avanti >', bg="lightgreen",command= lambda: self.avanti())
        btn_avanti.place(x = 1750, y= 850)
        
        btn_indietro=tk.Button(self, text='< indietro', bg="lightgreen",command=lambda: self.indietro())
        btn_indietro.place(x = 1650, y= 850)

        btn_consegna = tk.Button(self, text='consegna test', bg="lightgreen",command=self.consegna)
        btn_consegna.place(x = 1000, y= 850)

        exit_btn = tk.Button(self, text='esci dall\'esercitazione', bg="lightgreen",command= self.destroy)
        exit_btn.place(x = 100, y= 890)
        

    #metodo per avviare il timer
    def start_timer(self):
        if self.secondi > 0:
            self.min_restanti = self.secondi // 60
            self.sec_restanti = self.secondi % 60
            self.label_timer.config(text=f'{self.min_restanti:02d}:{self.sec_restanti:02d}')
            self.secondi -= 1
            self.after(1000, self.start_timer)
        else:
            messagebox.showinfo("TEMPO SCADUTO", "test consegnato")
            self.cons = True
            self.consegna()  #consegna automaticamente allo scadere del timer

    #metodo per saltare alla domanda scelta
    def vai_alla_domanda(self, indice):
        self.i = indice   
        self.label_domande.config(text=self.d[self.i][1])
        self.label_n_domande.config(text= f"Domande:\n{self.i + 1} / {self.N}")
        self.carica_immagine()

        self.chk_vero.config(variable=self.var_risposta[self.i])
        self.chk_falso.config(variable=self.var_risposta[self.i])

        print(self.i)

    #metodo per caricare l'immagine
    def carica_immagine(self):
        try:
            immagine = self.d[self.i][3]   
            self.img_tk = tk.PhotoImage(file=immagine)
            self.label_img.config(image=self.img_tk, text='') 
        except:
            self.label_img.config(image='', text='Errore durante il caricamento dell\'immagine')
    
    def consegna(self):
        for i in range(len(self.d)):
            if self.var_risposta[i].get() == 1 and self.d[i][2] == 'vero' or self.var_risposta[i].get() == 2 and self.d[i][2] == 'falso':
                self.punteggio += 1

        for j in range(self.N):
            if self.var_risposta[j].get() == 0:
                self.check = True
                break

        if self.cons == False:

            risposta = messagebox.askokcancel(title='consegna test', message=f'Vuoi consegnare il test?\n hai risposto a tutte le domande' if self.check == False else f'Sicuro di voler consegnare il test?\n non hai risposto a tutte le domande' )

            if risposta:
                messagebox.showinfo("TEST COMPLETATO",
                                    f'Hai superato il test:\n\nrisposte corrette: {self.punteggio}' if self.punteggio >= 27 else f'Non hai superato il test:\nrisposte giuste:{self.punteggio}')             
                self.destroy() 
        else:
            messagebox.showinfo("TEST COMPLETATO",
                                    f'Hai superato il test:\n\nrisposte corrette: {self.punteggio}' if self.punteggio >= 27 else f'Non hai superato il test:\nrisposte giuste:{self.punteggio}')             
  
            self.destroy()   


    def avanti(self): 
        if self.i < self.N:
            self.i+= 1   
            self.label_domande.config(text=self.d[self.i][1])
            self.label_n_domande.config(text= f"Domande:\n{self.i+1} / {self.N}")
            self.carica_immagine()

            self.chk_vero.config(variable=self.var_risposta[self.i])
            self.chk_falso.config(variable=self.var_risposta[self.i])

            # print(self.d[self.i][1])
            print(self.i)
        else: 
            messagebox.showerror("DOMANDE TERMINATE",
                                    "consegna il test o ricontrolla le domande")        

    def indietro(self): 
        if self.i > 0: 
            self.i-= 1   
            self.label_domande.config(text=self.d[self.i][1])
            self.label_n_domande.config(text= f"Domande:\n{self.i+1} / {self.N}")
            self.carica_immagine()

            self.chk_vero.config(variable=self.var_risposta[self.i])
            self.chk_falso.config(variable=self.var_risposta[self.i])

            # print(self.d[self.i][1])
        else:
            messagebox.showerror("impossibile tornare indietro",
                                    "sei già alla prima domanda")
        print(self.i)


def main_esercitazioni(argomento):
    f = Esercitazioni(argomento)
    f.title('Scheda esercitazione')
    f.geometry('1920x1080')
    f.resizable(0, 0)
    f.mainloop()

def main_scheda():
    f = Quiz()
    f.title('Scheda d\'esame')
    f.geometry('1920x1080')
    f.resizable(0, 0)
    f.mainloop()
    
def main():
    f = Home()
    f.master.title('Quiz patente B')
    f.master.geometry('1920x1080')
    f.master.resizable(0, 0)
    f.mainloop()

main()
