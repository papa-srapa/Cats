from tkinter import *
import requests  # отправляет HTTP запросы и получает ответ
from PIL import Image, ImageTk  # Для работы с изображением
from io import BytesIO  # Позволяет работать для ввода и вывода информации


def load_image():
    try:
        responses = requests.get(url)  # Получаем URL адрес
        responses.raise_for_status()  # Для обработки исключений
        image_data = BytesIO(responses.content)  # Тут храниться обработанное изображение
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None



window = Tk()
window.title('Cats')
window.geometry('600X480')

label = Label(text='')
label.pack()


url = 'https://cataas.com/cat'
img = load.image(url)

if img:  # Если переменная не пустая
    label.config(image=img)  # То устанавливаем картинку на метку
    label.image = img  # Что бы сборщик мусора не удалил картинку


window.mainloop()

