# view.py

from tkinter import *

class FlashCardView:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg="#B1DDC6")

        # Cria o canvas e configura a imagem do cartão com highlightthickness=0
        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
        self.imgEnglish = PhotoImage(file="Images/card_front.png")
        self.imgPortuguese = PhotoImage(file="Images/card_back.png")
        self.card_bg = self.canvas.create_image(400, 263, image=self.imgEnglish)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=3)

        # Botões de acerto e erro
        self.bt_wrong_img = PhotoImage(file="Images/wrong.png")
        self.bt_wrong = Button(image=self.bt_wrong_img, highlightthickness=0)
        self.bt_wrong.grid(row=1, column=0)

        self.bt_right_img = PhotoImage(file="Images/right.png")
        self.bt_right = Button(image=self.bt_right_img, highlightthickness=0)
        self.bt_right.grid(row=1, column=1)

        # Botão de Reiniciar Progresso
        self.bt_reset_img = PhotoImage(file="Images/reset_3.png")
        self.bt_reset_img_resized = self.bt_reset_img.subsample(28, 28)
        self.bt_reset = Button(image=self.bt_reset_img_resized, highlightthickness=0, bg="#B1DDC6")
        self.bt_reset.grid(row=1, column=2)

        # Rótulo de Progresso
        self.progress_label = Label(text="Progresso: 0/0", bg="#B1DDC6", font=("Arial", 16))
        self.progress_label.grid(row=2, column=0, columnspan=3)

    def setup_button_commands(self):
        """Atribui os comandos dos botões."""
        self.bt_wrong.config(command=lambda: [self.controller.unknown_word(), self.provide_feedback("red")])
        self.bt_right.config(command=lambda: [self.controller.known_word(), self.provide_feedback("green")])
        self.bt_reset.config(command=self.controller.reset_progress)

    def update_card(self, title, word, img, color):
        """Atualiza o conteúdo do cartão."""
        self.canvas.itemconfig(self.card_bg, image=img)
        self.canvas.itemconfig(self.card_title, text=title, fill=color)
        self.canvas.itemconfig(self.card_word, text=word, fill=color)

    def schedule_flip(self, callback):
        """Agenda a virada do cartão após 3 segundos."""
        self.window.after(3000, callback)

    def provide_feedback(self, color):
        """Altera a cor de fundo do cartão para dar feedback visual."""
        self.canvas.config(bg=color)
        self.window.after(500, lambda: self.canvas.config(bg="#B1DDC6"))

    def show_no_words_message(self):
        """Exibe mensagem de fim de palavras."""
        self.canvas.itemconfig(self.card_title, text="No more words", fill="black")
        self.canvas.itemconfig(self.card_word, text="", fill="black")

    def update_progress(self, learned, total):
        """Atualiza o rótulo de progresso."""
        self.progress_label.config(text=f"Progresso: {learned}/{total}")



















