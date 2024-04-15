import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password():
    length = int(length_entry.get())

    if length < 4:
        result_label.config(text="Длина пароля должна быть не менее 4 символов", foreground="red")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    result_label.config(text=f"Сгенерированный пароль: {password}", foreground="green")


# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")

# Добавление виджетов на главное окно
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(frame, text="Длина пароля:")
length_label.grid(row=0, column=0, sticky=tk.W)

length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, sticky=tk.W)

generate_button = ttk.Button(frame, text="Сгенерировать", command=generate_password)
generate_button.grid(row=1, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, columnspan=2)

# Запуск главного цикла
root.mainloop()




