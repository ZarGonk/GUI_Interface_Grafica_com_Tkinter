import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # -------------------- JANELA --------------------
        self.title("List Fruits - Modern UI")
        self.geometry("350x350")
        self.configure(bg="#1e1e1e")  # fundo dark

        # -------------------- ESTILO --------------------
        style = ttk.Style(self)
        style.theme_use("clam")

        # Label padrão
        style.configure("TLabel",
                        background="#1e1e1e",
                        foreground="#ffffff",
                        font=("Segoe UI", 12))

        # Label título
        style.configure("Title.TLabel",
                        background="#1e1e1e",
                        foreground="#00c8ff",
                        font=("Segoe UI Semibold", 16))

        # Frame estilizado
        style.configure("Card.TFrame",
                        background="#2b2b2b",
                        borderwidth=0,
                        relief="flat")

        # Listbox estilo dark (Listbox é Tk, não ttk)
        self.listbox_bg = "#2b2b2b"
        self.listbox_fg = "#ffffff"
        self.listbox_select = "#00c8ff"

        # -------------------- TÍTULO --------------------
        self.title_label = ttk.Label(self,
                                     text="Selecione suas frutas",
                                     style="Title.TLabel")
        self.title_label.pack(pady=15)

        # -------------------- CARD (FRAME) --------------------
        self.card = ttk.Frame(self, style="Card.TFrame", padding=10)
        self.card.pack(padx=15, pady=10, fill="both", expand=True)

        # Lista de frutas
        fruts = [
            'Abacaxi', 'Banana', 'Caju', 'Damasco', 'Figo',
            'Goiaba', 'Jabuticaba', 'Kiwi', 'Laranja', 'Manga',
            'Nectarina', 'Oliva', 'Pera', 'Quivi', 'Romã'
        ]

        list_fruts = tk.Variable(value=fruts)

        # -------------------- LISTBOX --------------------
        self.listbox = tk.Listbox(self.card,
                                  listvariable=list_fruts,
                                  height=6,
                                  selectmode="multiple",
                                  bg=self.listbox_bg,
                                  fg=self.listbox_fg,
                                  selectbackground=self.listbox_select,
                                  selectforeground="#000000",
                                  highlightthickness=0,
                                  relief="flat",
                                  font=("Segoe UI", 11))
        self.listbox.pack(fill="both", expand=True)

        # Evento de seleção
        self.listbox.bind("<<ListboxSelect>>", self.handle_selection)

        # -------------------- RESULTADO --------------------
        self.result_label = ttk.Label(self,
                                      text="Nenhuma fruta selecionada",
                                      font=("Segoe UI", 12))
        self.result_label.pack(pady=10)

    def handle_selection(self, event):
        selected_indices = self.listbox.curselection()
        selected_fruts = [self.listbox.get(i) for i in selected_indices]

        texto = (
            "Nenhuma fruta selecionada"
            if not selected_fruts
            else "Selecionadas: " + ", ".join(selected_fruts)
        )

        self.result_label.config(text=texto)


if __name__ == "__main__":
    app = App()
    app.mainloop()
