import tkinter as tk
import re
from datetime import datetime


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot de Voyage")
        self.root.geometry("500x500")

        self.conversation_state = 0

        # Date
        date = datetime.now().strftime("%d/%m/%Y")
        self.date_label = tk.Label(root, text=f"Date : {date}")
        self.date_label.pack(pady=5)

        # Zone de texte
        self.txt = tk.Text(root, height=18, width=60, state=tk.NORMAL)
        self.txt.pack(pady=10)

        # Entrée utilisateur
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        # Bouton envoyer
        self.send_button = tk.Button(root, text="Envoyer", command=self.envoyer_message)
        self.send_button.pack(pady=5)

        # Message initial
        self.txt.insert(tk.END, "Chatbot: Bonjour ! Bienvenue sur l'assistant de voyage.\n")

    def envoyer_message(self):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.txt.insert(tk.END, f"Vous: {user_input}\n")
        self.entry.delete(0, tk.END)

        response = self.get_bot_response(user_input)
        self.txt.insert(tk.END, f"Chatbot: {response}\n")

    def get_bot_response(self, user_input):
        user_input = user_input.lower()

        if self.conversation_state == 0:
            self.conversation_state += 1
            return "Préférez-vous l'Afrique ou l'Europe ?"

        elif self.conversation_state == 1:
            if "afrique" in user_input:
                self.conversation_state += 1
                return "Je vous propose : Maroc ou Égypte."
            elif "europe" in user_input:
                self.conversation_state += 1
                return "Je vous propose : Espagne ou Italie."
            else:
                return "Veuillez choisir entre Afrique ou Europe."

        elif self.conversation_state == 2:
            if "maroc" in user_input:
                self.conversation_state += 1
                return "Au Maroc : Rabat, Tanger, Merzouga, Ifrane."
            elif "egypte" in user_input:
                self.conversation_state += 1
                return "En Égypte : Pyramides, Louxor."
            elif "espagne" in user_input:
                self.conversation_state += 1
                return "En Espagne : Madrid, Séville, Barcelone."
            elif "italie" in user_input:
                self.conversation_state += 1
                return "En Italie : Rome, Venise."
            else:
                return "Choisissez : Maroc, Égypte, Espagne ou Italie."

        elif self.conversation_state == 3:
            if "hotel" in user_input:
                self.conversation_state += 1
                return "Voulez-vous réserver ? tapez 'réserver' pour continuer."
            else:
                return "Tapez 'hotel' pour voir les hôtels."

        elif self.conversation_state == 4:
            if "réserver" in user_input:
                self.conversation_state += 1
                return "Entrez : Nom, Prénom, Téléphone, CIN"
            else:
                return "D'accord, bon voyage !"

        elif self.conversation_state == 5:
            try:
                name, prenom, numero, cin = [x.strip() for x in user_input.split(",")]

                if self.validate_phone(numero) and self.validate_cin(cin):
                    self.conversation_state += 1
                    return "Informations valides ✅"
                else:
                    return "Téléphone ou CIN invalide ❌"

            except ValueError:
                return "Format invalide. Exemple: Nom, Prénom, Téléphone, CIN"

        else:
            return "Merci d'avoir utilisé le chatbot !"

    def validate_phone(self, numero):
        return re.match(r'^0[6-7][0-9]{8}$', numero) is not None

    def validate_cin(self, cin):
        return re.match(r'^[A-Z]{1,2}[0-9]{6}$', cin) is not None


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
