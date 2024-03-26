import customtkinter as ctk
from tkinter import messagebox, filedialog

class TextEncryptorApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Text Encryptor")
        self.geometry("800x600")


        self.entry_frame = ctk.CTkFrame(self, width=780, height=40, border_width=0)
        self.entry_frame.pack(pady=10)

        self.text_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter text to encrypt/decrypt", width=760, height=40,border_width=1)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)
        
        # Add right-click paste functionality
        self.text_entry.bind("<Button-3>", lambda e: self.text_entry.event_generate("<Control-v>"))

        self.button_frame = ctk.CTkFrame(self, width=780, height=40)
        self.button_frame.pack(padx=5, pady=10)

        self.encrypt_button = ctk.CTkButton(self.button_frame, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        self.decrypt_button = ctk.CTkButton(self.button_frame, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=2, padx=5, pady=10, sticky="ew")

        self.open_file_button = ctk.CTkButton(self.button_frame, text="Open File", command=self.open_file)
        self.open_file_button.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

        self.save_button = ctk.CTkButton(self.button_frame, text="Save", command=self.save)
        self.save_button.grid(row=0, column=4, padx=5, pady=10, sticky="ew")

        self.result = ctk.CTkTextbox(self, width=780, height=400)
        self.result.pack(padx=10, pady=10)

    def encrypt(self):
        """
        Encrypts the text using a cipher with a shift of 13.
        """
        text = self.text_entry.get()
        encrypted_text = self.apply_cipher(text, shift=13)
        self.display_result(encrypted_text)

    def decrypt(self):
        """
        Decrypts the text using a cipher with a shift of -13.

        Parameters:
            None

        Returns:
            None
        """
        text = self.text_entry.get()
        decrypted_text = self.apply_cipher(text, shift=-13)
        self.display_result(decrypted_text)

    def apply_cipher(self, text, shift):
        """
        Apply a cipher to the given text using the specified shift value.

        Parameters:
            text (str): The text to apply the cipher to.
            shift (int): The shift value to use for the cipher.

        Returns:
            str: The resulting text after applying the cipher.
        """
        result_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result_text += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result_text += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result_text += char
        return result_text

    def display_result(self, result):
        self.result.delete("1.0", ctk.END)
        self.result.insert(ctk.END, result)

    def clear(self):
        self.text_entry.delete("0", ctk.END)
        self.result.delete("1.0", ctk.END)

    def open_file(self):
        """
        Opens a file dialog to prompt the user to select a file. 
        If a file is selected, it reads the content of the file and inserts it into the text entry.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_entry.delete(0, ctk.END)
            self.text_entry.insert(0, content)

    def save(self):
        """
        Saves the text from the result widget to a file.

        Parameters:
            None

        Returns:
            None
        """
        text = self.result.get("1.0", ctk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
        self.result.delete("1.0", ctk.END)
        messagebox.showinfo("Success", "Text saved successfully!")



if __name__ == "__main__":
    app = TextEncryptorApp()
    app.mainloop()
