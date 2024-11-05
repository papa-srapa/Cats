from tkinter import *
import requests  # отправляет HTTP запросы и получает ответ
from PIL import Image, ImageTk  # Для работы с изображением
from io import BytesIO  # Позволяет работать для ввода и вывода информации


def load_image(url):
    try:
        responses = requests.get(url)  # Получаем URL адрес
        responses.raise_for_status()  # Для обработки исключений
        image_data = BytesIO(responses.content)  # Тут храниться обработанное изображение
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_image():  # Функция будет загружать новое изображение при нажатии кнопки
    img = load_image(url)

    if img:  # Если переменная не пустая
        label.config(image=img)  # То устанавливаем картинку на метку
        label.image = img  # Что бы сборщик мусора не удалил картинку


window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

update_button = Button(text='Обновить',command=set_image)
update_button.pack()



url = 'https://cataas.com/cat'

set_image()  # Вызываем функцию при запуске программы для появления первого изображения



window.mainloop()

