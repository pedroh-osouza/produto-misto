import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from Properties import Properties
from Arrays3D import Arrays3D

global u, w, v
class Window(tk.Toplevel):
    def __init__(self, parent,u,v,w):
        super().__init__(parent)
        def one(): 
            messagebox.showinfo("Propriedade 1", Properties(u,v,w).one() ) 
        def two(): 
            messagebox.showinfo("Propriedade 2", Properties(u,v,w).two()) 
        def three(): 
            messagebox.showinfo("Propriedade 3",Properties(u,v,w).three()) 
        def four(): 
            messagebox.showinfo("Propriedade 4",Properties(u,v,w).four()) 
        def five(): 
            messagebox.showinfo("Propriedade 5",Properties(u,v,w).five()) 
        def six(): 
            messagebox.showinfo("Propriedade 6",Properties(u,v,w).six()) 
        def seven(): 
            messagebox.showinfo("Propriedade 7",str(Properties(u,v,w).seven())) 
        def eigth(): 
            messagebox.showinfo("Propriedade 8",Properties(u,v,w).eight()) 
        def nine(): 
            messagebox.showinfo("Definição",'O produto misto dos vetores u, v, w (nesta ordem é o número real [u, v, w] = u ^ v * w).') 
            

        self.geometry('450x170')
        self.title(' Selecione a Propriedade:')
        create_vet1 = tk.Button(self,text='Propriedade um: ', command= one)
        create_vet1.grid(row=1, column=0, padx=10, pady=10)
        create_vet2 = tk.Button(self ,text='Propriedade dois: ', command= two)
        create_vet2.grid(row=2, column=0, padx=10, pady=10)
        create_vet3 = tk.Button(self, text='Propriedade três:', command= three)
        create_vet3.grid(row=3, column=0, padx=10, pady=10)
        create_vet4 = tk.Button(self, text='Propriedade quatro: ', command= four)
        create_vet4.grid(row=1, column=1, padx=10, pady=10)
        create_vet5 = tk.Button(self,text='Propriedade cinco: ', command= five) 
        create_vet5.grid(row=2, column=1, padx=10, pady=10)
        create_vet6 = tk.Button(self,text='Propriedade seis:', command=six)
        create_vet6.grid(row=3, column=1, padx=10, pady=10)
        create_vet7 = tk.Button(self,text='Propriedade sete:', command=seven)
        create_vet7.grid(row=1, column=2, padx=10, pady=10)
        create_vet8 = tk.Button(self, text='Propriedade oito: ', command=eigth)
        create_vet8.grid(row=2, column=2, padx=10, pady=10)
        create_vet9 = tk.Button(self, text='Definição Produto Misto: ', command=nine)
        create_vet9.grid(row=3, column=2, padx=10, pady=10)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        def create_vetor():
            u = Arrays3D(int(v11e.get()), int(v12e.get()), int(v13e.get())).array
            print(u)
            v = Arrays3D(int(v21e.get()), int(v22e.get()), int(v23e.get())).array
            print(v)
            w = Arrays3D(int(v31e.get()), int(v32e.get()), int(v33e.get())).array
            print(w)

            window = Window(self,u,v,w)
            window.grab_set()


        self.geometry('500x600')
        self.title('Produto Misto')
        lable = tk.Label(self, text="VETOR 1 ")
        lable.grid(row=0, column=1, padx=5, pady=10)
        ##################################################################
        v11 = tk.Label(self, text='Primeiro número: ')
        v11.grid(row=1, column=0, padx=10, pady=10) 
        v12 = tk.Label(self, text=' Segundo número: ')
        v12.grid(row=2, column=0, padx=10, pady=10) 
        v13 = tk.Label(self, text='Terceiro número: ')
        v13.grid(row=3, column=0, padx=10, pady=10)
        ##################################################################
        v11e = tk.Entry(self, width=35)
        v11e.grid(row=1, column=1, padx=10, pady=10)    
        v12e = tk.Entry(self, width=35)
        v12e.grid(row=2, column=1, padx=10, pady=10)    
        v13e = tk.Entry(self, width=35)
        v13e.grid(row=3, column=1, padx=10, pady=10)
        #################################################################
        lable1 = tk.Label(self, text="VETOR 2 ")
        lable1.grid(row=4, column=1, padx=5, pady=10)
        ##################################################################
        v21 = tk.Label(self, text='Primeiro número: ')
        v21.grid(row=5, column=0, padx=10, pady=10) 
        v22 = tk.Label(self, text=' Segundo número: ')
        v22.grid(row=6, column=0, padx=10, pady=10) 
        v23 = tk.Label(self, text='Terceiro número: ')
        v23.grid(row=7, column=0, padx=10, pady=10)
        ################################################################
        v21e = tk.Entry(self, width=35)
        v21e.grid(row=5, column=1, padx=10, pady=10)    
        v22e = tk.Entry(self, width=35)
        v22e.grid(row=6, column=1, padx=10, pady=10)    
        v23e = tk.Entry(self, width=35)
        v23e.grid(row=7, column=1, padx=10, pady=10)
        ############################################################
        lable1 = tk.Label(self, text="VETOR 3 ")
        lable1.grid(row=8, column=1, padx=5, pady=10)
        ##################################################################
        v31 = tk.Label(self, text='Primeiro número: ')
        v31.grid(row=9, column=0, padx=10, pady=10) 
        v32 = tk.Label(self, text=' Segundo número: ')
        v32.grid(row=10, column=0, padx=10, pady=10)    
        v33 = tk.Label(self, text='Terceiro número: ')
        v33.grid(row=11, column=0, padx=10, pady=10)
        ################################################################
        v31e = tk.Entry(self, width=35)
        v31e.grid(row=9, column=1, padx=10, pady=10)    
        v32e = tk.Entry(self, width=35)
        v32e.grid(row=10, column=1, padx=10, pady=10)   
        v33e = tk.Entry(self, width=35)
        v33e.grid(row=11, column=1, padx=10, pady=10)
        ############################################################    
        create_vet = tk.Button(text='Cadastrar Vetores', command=create_vetor)
        create_vet.grid(row=12, column=1, padx=10, pady=10)
   


if __name__ == "__main__":
    app = App()
    app.mainloop()