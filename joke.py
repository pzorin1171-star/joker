import time
import random
import tkinter as tk
from tkinter import messagebox
import sys

wrong_attempts = 0

def cheking():
    global wrong_attempts
    user_input = entry.get()
    
    funny_responses = [
        "Неправильно! Система нагревается...",
        "Ошибка доступа! Запускаю протокол самоуничтожения...",
        "Не-а! Попробуй еще раз, если осмелишься!",
        "Хакерская атака обнаружена! Блокирую систему...",
        "Доступ запрещен! Уровень угрозы: КРИТИЧЕСКИЙ",
        "Пароль неверный! Активирую систему защиты...",
        "Ты думаешь это так просто? Ха-ха-ха!",
        "Нет-нет-нет! Миссия невыполнима!"
    ]
    
    messagebox.showwarning("ОШИБКА", random.choice(funny_responses))
    
    wrong_attempts += 1
    
    if wrong_attempts == 3:
        create_fake_error()
    elif wrong_attempts == 5:
        create_moving_button()
    elif wrong_attempts == 7:
        start_matrix_rain()
    elif wrong_attempts == 10:
        messagebox.showerror("КРИТИЧЕСКИЙ СБОЙ", "Система нестабильна! Перезагрузка невозможна!")
    
    entry.delete(0, tk.END)

def do_nothing():
    fake_messages = [
        "Нет уж, ты останешься здесь!",
        "Попытка отклонена!",
        "Хорошая попытка! Но нет.",
        "Система заблокирована. Выход невозможен.",
        "А ты хитрый! Но не сработает."
    ]
    messagebox.showinfo("Ой!", random.choice(fake_messages))

def create_fake_error():
    error_window = tk.Toplevel(root)
    error_window.title("Системная ошибка")
    error_window.geometry("300x150")
    error_window.attributes("-topmost", True)
    center_window(error_window)
    
    tk.Label(error_window, text="ОШИБКА 0x80070005", fg="red", font=("Arial", 12)).pack(pady=10)
    tk.Label(error_window, text="Доступ к памяти запрещен", font=("Arial", 10)).pack()
    tk.Button(error_window, text="OK", command=error_window.destroy).pack(pady=20)

def create_moving_button():
    def move_button():
        x = random.randint(50, 350)
        y = random.randint(50, 350)
        moving_btn.place(x=x, y=y)
    
    moving_window = tk.Toplevel(root)
    moving_window.title("Подтверждение выхода")
    moving_window.geometry("400x400")
    moving_window.attributes("-topmost", True)
    center_window(moving_window)
    
    tk.Label(moving_window, text="Вы уверены, что хотите выйти?", font=("Arial", 12)).pack(pady=20)
    
    moving_btn = tk.Button(moving_window, text="ДА", command=do_nothing)
    moving_btn.pack()
    
    moving_btn.bind("<Enter>", lambda e: move_button())

def start_matrix_rain():
    canvas = tk.Canvas(root, bg='black', highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    
    chars = "01010101010101010101010101010101"
    columns = root.winfo_screenwidth() // 20
    drops = [1] * columns
    
    def rain():
        canvas.delete("matrix")
        for i in range(columns):
            x = i * 20
            y = drops[i] * 20
            
            char = random.choice(chars)
            color = "#00FF00" if random.random() > 0.1 else "#008000"
            
            canvas.create_text(x, y, text=char, fill=color, font=("Courier", 12), tags="matrix")
            
            if y > root.winfo_screenheight() or random.random() > 0.95:
                drops[i] = 0
            drops[i] += 1
        
        root.after(50, rain)
    
    rain()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = tk.Tk()
root.title("СИСТЕМНАЯ БЕЗОПАСНОСТЬ")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg='#000000')
root.protocol("WM_DELETE_WINDOW", do_nothing)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

main_frame = tk.Frame(root, bg='#000000')
main_frame.place(relx=0.5, rely=0.5, anchor='center')

title_label = tk.Label(main_frame, text="=== СИСТЕМА БЕЗОПАСНОСТИ ===", 
                      fg="#00FF00", bg="#000000", font=("Courier", 24))
title_label.pack(pady=20)

instruction = tk.Label(main_frame, text="ДЛЯ ВЫХОДА ИЗ СИСТЕМЫ ВВЕДИТЕ ПАРОЛЬ АДМИНИСТРАТОРА", 
                      fg="#FFFFFF", bg="#000000", font=("Arial", 16))
instruction.pack(pady=15)

warning = tk.Label(main_frame, text="ПРЕДУПРЕЖДЕНИЕ: НЕПРАВИЛЬНЫЙ ПАРОЛЬ МОЖЕТ ВЫЗВАТЬ НЕПРЕДСКАЗУЕМЫЕ ПОСЛЕДСТВИЯ!", 
                  fg="#FF0000", bg="#000000", font=("Arial", 12))
warning.pack(pady=10)

entry = tk.Entry(main_frame, bg="#000000", fg="#00FF00", font=("Courier", 18), 
                show="*", width=30, justify='center', insertbackground='#00FF00')
entry.pack(pady=25)

entry.focus_set()

entry.bind('<Return>', lambda event: cheking())

checker = tk.Button(main_frame, text="ПРОВЕРИТЬ ПАРОЛЬ", bg="#FF0000", fg="#FFFFFF", 
                   font=("Arial", 14), command=cheking)
checker.pack(pady=15)

def fake_calculations():
    calculations = [
        "Сканирование памяти...",
        "Проверка системных файлов...", 
        "Анализ угроз безопасности...",
        "Мониторинг сетевой активности...",
        "Проверка целостности данных...",
        "Оптимизация процессов..."
    ]
    calc_label.config(text=random.choice(calculations))
    root.after(2000, fake_calculations)

calc_label = tk.Label(main_frame, text="Сканирование системы...", fg="#FFFF00", bg="#000000", font=("Arial", 10))
calc_label.pack(pady=10)

exit_hint = tk.Label(root, text="Подсказка: попробуйте Ctrl+Shift+Esc", 
                    fg="#333333", bg="#000000", font=("Arial", 8))
exit_hint.place(relx=0.5, rely=0.95, anchor='center')

fake_calculations()

root.mainloop()

print("Поздравляю! Вы пережили шутку!")
print("На самом деле, чтобы выйти, нужно было:")
print("1. Нажать Alt+F4") 
print("2. Или запустить Диспетчер задач (Ctrl+Shift+Esc)")
print("3. Или просто перезагрузить компьютер")
print("ЛОЛ")
