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
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)  # Подгоняем все изображения под один размер
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def set_image():  # Функция будет загружать новое изображение при нажатии кнопки
    img = load_image(url)

    if img:  # Если переменная не пустая
        label.config(image=img)  # То устанавливаем картинку на метку
        label.image = img  # Что бы сборщик мусора не удалил картинку


def exit_1():
    window.destroy()  # Завершаем работу программы


window = Tk()
window.title('Cats')
window.geometry('600x520')

menu_bar = Menu(window)
window.config(menu=menu_bar)


file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='выход', command=exit_1)

label = Label()
label.pack()


# menu_bar = Menu(window)
# window.config(menu=menu_bar)


# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label='Файл', menu=file_menu)
# file_menu.add_command(label='Загрузить фото', command=set_image)
# file_menu.add_separator()
# file_menu.add_command(label='выход', command=exit_1)



# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label='Файл', menu=file_menu)
# file_menu.add_command(label='Загрузить фото', command=set_image)
# file_menu.add_separator()
# file_menu.add_command(label='выход', command=exit_1)

# update_button = Button(text='Обновить', command=set_image)
# update_button.pack()



url = 'https://cataas.com/cat/cute'
set_image()  # Вызываем функцию при запуске программы для появления первого изображения


window.mainloop()

