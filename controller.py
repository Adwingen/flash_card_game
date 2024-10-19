# controller.py

class FlashCardController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_word = {}

        # Atualiza o progresso inicial
        self.update_progress()

    def generate_new_word(self):
        """Gera uma nova palavra em inglês e agenda a virada do cartão."""
        word_pair = self.model.get_random_word()
        if word_pair:
            self.current_word = word_pair  # Armazena a palavra atual para referência ao virar o cartão
            self.view.update_card("English", word_pair["English"], self.view.imgEnglish, "black")
            self.view.schedule_flip(self.flip_card)
        else:
            self.view.show_no_words_message()

    def flip_card(self):
        """Vira o cartão para mostrar a tradução em português."""
        if self.current_word:
            self.view.update_card("Portuguese", self.current_word["Portuguese"], self.view.imgPortuguese, "white")

    def known_word(self):
        """Remove a palavra atual da lista ao clicar no botão ✅ e gera nova palavra."""
        self.model.remove_current_word()
        self.generate_new_word()
        self.update_progress()

    def unknown_word(self):
        """Gera uma nova palavra ao clicar no botão ❌ sem remover a palavra atual."""
        self.generate_new_word()

    def update_progress(self):
        """Atualiza o rótulo de progresso."""
        learned = self.model.get_learned_count()
        total = self.model.get_total_count()
        self.view.update_progress(learned, total)

    def reset_progress(self):
        """Reinicia o progresso, restaurando as palavras originais."""
        self.model.reset_words()
        self.generate_new_word()
        self.update_progress()






