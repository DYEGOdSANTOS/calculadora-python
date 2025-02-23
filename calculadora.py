import tkinter as tk   

class Calculadora:
    def __int__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.resultado = tk.StringVar()

        self.criar_tela()
        self.criar_botoes()  #erro aqui

    def criar_tela(self):
        tela = tk.Entry(self.root, textvariable=self.resultado, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        tela.grid(row=0, column=0, columnspan=4)

        def criar_botoes(self):
            botoes = ['7','8','9','/',
                      '4', '5','6','*'
                      '1','2','3','-'
                      'C','0','=','+'
                      ]
            
            linha = 1
            coluna = 0


            for botao in botoes:
                comando = lambda x=botao: self.clique_botao(x)
                tk.Button(self.root, text=botao, font=('Arial', 18), command=comando,width=5, height=2).grid(row=linha, column=coluna)
                coluna +=1
                if coluna > 3:
                    coluna = 0 
                    linha += 1

        def clique_botao(self, valor):
            if valor == 'C':
                self.resultado.set('')
            elif valor == '=':
                try:
                    resultado = str(eval(self.resultado.get()))
                    self.resultado.set(resultado)
                except:
                        self.resultado.set('Erro')
                else:
                    self.resultado.set(self.resultado.get() + valor)

        if __name__== "__main__":
            root = tk.Tk()
            calc = Calculadora(root)
            root.mainloop()
