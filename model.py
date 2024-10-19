# model.py

import pandas as pd
import os
from random import choice

class FlashCardModel:
    def __init__(self):
        self.words_to_learn = "Data/words_to_learn.csv"
        self.default_words = "Data/english_words.csv"
        self.file_to_dic = []
        self.current_word = {}

        # Palavras já aprendidas
        self.learned_words = 0

        # Carregar o arquivo words_to_learn.csv ou english_words.csv
        self.load_words()

    def load_words(self):
        """Carrega as palavras do arquivo words_to_learn.csv se existir, caso contrário, do arquivo original."""
        try:
            if os.path.exists(self.words_to_learn):
                self.file = pd.read_csv(self.words_to_learn)
            else:
                self.file = pd.read_csv(self.default_words)
            self.file_to_dic = self.file.to_dict(orient="records")
        except FileNotFoundError:
            print(f"Arquivo {self.default_words} não encontrado!")
            self.file_to_dic = []

    def get_random_word(self):
        """Escolhe uma palavra aleatória da lista."""
        if self.file_to_dic:
            self.current_word = choice(self.file_to_dic)
            return self.current_word
        else:
            return None

    def remove_current_word(self):
        """Remove a palavra atual da lista e salva as palavras restantes."""
        if self.current_word in self.file_to_dic:
            self.file_to_dic.remove(self.current_word)
            new_data = pd.DataFrame(self.file_to_dic)
            new_data.to_csv(self.words_to_learn, index=False)
            self.learned_words += 1  # Incrementa o contador de palavras aprendidas

    def get_learned_count(self):
        """Retorna o número de palavras aprendidas."""
        return self.learned_words

    def get_total_count(self):
        """Retorna o total de palavras a aprender."""
        return len(self.file_to_dic) + self.learned_words

    def reset_words(self):
        """Reinicia a lista de palavras, voltando para o arquivo original."""
        self.learned_words = 0
        self.load_words()









