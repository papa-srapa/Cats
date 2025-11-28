from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = b_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x300")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



def exchange():
    code = entry.get().lower()  # Получаем введённый код и преобразуем его к нижнему регистру
    if code:  # Если код есть (введён)
        try:
            # Запрос к API для получения курса криптовалюты к доллару
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={code}&vs_currencies=usd")
            response.raise_for_status()  # Проверяем на ошибки в ответе
            data = response.json()
            if code in data:  # Проверяем, существует ли код в данных
                exchange_rate = data[code]['usd']  # Получаем курс к доллару
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate} USD за 1 {code.capitalize()}")
            else:
                mb.showerror("Ошибка!", f"Криптовалюта {code} не найдена!")
        except requests.exceptions.RequestException as e:
            mb.showerror("Ошибка сети", f"Произошла ошибка с сетью: {e}.")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код криптовалюты.")


# Создание окна
window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x180")
window['bg'] = 'black'


Label(text="Введите код криптовалюты", background='green', foreground='black').pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", bg='black', foreground='black', command=exchange).pack(padx=10, pady=10)

window.mainloop()
