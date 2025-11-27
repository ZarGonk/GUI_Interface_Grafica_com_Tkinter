import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações principais da janela
        self.title("Exemplo de Diálogo YES/NO")
        self.geometry("300x200")

        # Label de título
        label = tk.Label(self, text="Confirmações com Tkinter")
        label.grid(row=0, column=0, columnspan=3, pady=10)

        # Botão que usa askyesno (retorna True/False)
        button_yesno = ttk.Button(self, text="Usar askyesno", command=self.confirm_yesno)
        button_yesno.grid(row=1, column=0, columnspan=3, pady=5)

        # Botão que usa askquestion (retorna 'yes' ou 'no')
        button_question = ttk.Button(self, text="Usar askquestion", command=self.confirm_question)
        button_question.grid(row=2, column=0, columnspan=3, pady=5)

        # Ajuste de proporção das colunas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def confirm_yesno(self):
        """
        Exibe uma caixa de diálogo de confirmação usando askyesno.
        Retorno: True (Yes) ou False (No).
        """
        answer = askyesno(title="Confirmação", message="Deseja realmente sair?")
        if answer:
            self.destroy()

    def confirm_question(self):
        """
        Exibe uma caixa de diálogo de confirmação usando askquestion.
        Retorno: 'yes' ou 'no' (string).
        """
        answer = askquestion(title="Confirmação", message="Deseja continuar?")
        print(f"Resposta: {answer}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
