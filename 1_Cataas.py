from tkinter import *
import requests  # отправляет HTTP запросы и получает ответ
from PIL import Image, ImageTk  # Для работы с изображением
from io import BytesIO  # Позволяет работать для ввода и вывода информации


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

