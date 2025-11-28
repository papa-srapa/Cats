import json
from tkinter import *
import requests  # отправляет HTTP запросы и получает ответ
from tkinter import messagebox as mb
from tkinter import ttk


def excheng():
    currency_code = combobox.get().lower()  # Получаем информацию с поля ввода
    if currency_code:
        try:  # Получаем ответ с сайта
            response = requests.get(
                f"https://api.coingecko.com/api/v3/simple/price?ids={currency_code}&vs_currencies=usd")
            response.raise_for_status()  # Проверяем полученную информацию на ошибки
            data = response.json()  # Сохраняем ответ в виде словаря
            if currency_code in data:  # Проверяем, существует ли код в данных
                ex_rase = data[currency_code]['usd']  # Сохраняем нужный нам курс
                mb.showinfo('Курс обмена', f'Курс обмена: {ex_rase} $USD за 1 {currency_code}')
            else:
                mb.showerror('Ошибка', f'Криптовалюта {currency_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}.')
    else:
        mb.showwarning('Внимание', 'В поле ввода отсутствует информация')


window = Tk()  # Создание окна
window.title('Курс криптовалют к USDT')
window.geometry('380x400')  # Размер главного окна
window['bg'] = 'black'  # Цвет главного окна

Label(text='Выберите  нужную криптовалюты', font=("TkDefaultFont", 15), fg='lime').pack(padx=10, pady=10)

currency = ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano', ]  # Выпадающий список
combobox = ttk.Combobox(values=currency,)  # Для функционирования выпадающего списка
combobox.pack()


Button(text='Получить курс', font=("system", 15), fg="black", bg="yellow", command=excheng).pack(padx=10, pady=10)


window.mainloop()
