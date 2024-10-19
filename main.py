from model import FlashCardModel
from view import FlashCardView
from controller import FlashCardController

def main():
    # Inicializa o Model
    model = FlashCardModel()

    # Cria a View sem controller inicialmente
    view = FlashCardView(controller=None)

    # Inicializa o Controller e passa o Model e a View
    controller = FlashCardController(model, view)

    # Agora, conecte a View com o Controller
    view.controller = controller

    # Configure os comandos dos botões agora que o controller está atribuído
    view.setup_button_commands()

    # Inicia automaticamente o primeiro flashcard após 1 segundo
    view.window.after(2000, controller.generate_new_word)

    # Inicia o loop principal
    view.window.mainloop()

if __name__ == "__main__":
    main()











