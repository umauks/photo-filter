import os
from filters import Red
from filters import Blue
from filters import Green
from filters import Dark
from filters import Bright
from filters import Inverse
from PIL import Image

filters = {
    1: {
        "name": "Red_filter",
        "description": "Изображение становится красным.",
        "function": Red()
    },
    2: {
        "name": "Blue_filter",
        "description": "Изображение становится синим.",
        "function": Blue()
    },
    3: {
        "name": "Green_filter",
        "description": "Изображение становится зеленым.",
        "function": Green()
    },
    4: {
        "name": "Dark_filter",
        "description": "Изображение становится темным.",
        "function": Dark()
    },
    5: {
        "name": "Bright_filter",
        "description": "Изображение становится светлым.",
        "function": Bright()
    },
    6: {
        "name": "Inverse_filter",
        "description": "Изображение инвертируется.",
        "function": Inverse()
    },
    0: {
        "name": "Выход"
    }
}
#меню фильтров
def menu():
    '''Выводит меню фильтров.'''
    print('Меню фильтров:')
    for i in range(len(filters)):
        print(f"{i}: {filters[i]['name']}")

finished = False
while not finished:
    print('Добро пожаловать в консольный фоторедактор.')

    #путь к файлу
    path = input('Введите путь к файлу или exit для выхода: ')
    if path == 'exit':
        quit()
    while not os.path.exists(path):
        path = input('Файл не найден. Попробуйте еще раз: ')
        if path == 'exit':
            quit()
    img = Image.open(path).convert("RGB")
    menu()

    #выбор фильтр
    number = input("Выберите номер фильтра (или 0 для выхода): ")
    while not 0 < int(number) <= len(filters) - 1 and number != 0:
        number = input("Некорректный ввод. Попробуйте ещё раз: ")
    if number == 0:
        print('Пока!')
        quit()
    else:
        print(f'{filters[int(number)]["name"]}: {filters[int(number)]["description"]}')

    #применить фильтр или нет
    yes_no = input('Применить фильтр к изображению? да/нет: ')

    while yes_no.lower() != "нет" and yes_no.lower() != "да":
        yes_no = input('Некорректно введено значение. Попробуй еще раз: ')
    finished = yes_no == 'нет'

    if yes_no.lower() == "да":
        filt = filters[int(number)]['function']
        img_new = filt.ap_image(img)

        # сохраняем
        save_path = input('Куда сохранить: ')
        img_new.save(save_path)


    #повторить еще раз или нет
    yesno = input('Еще раз?: ')
    while yesno.lower() != "да" and yesno.lower() != "нет":
        yesno = input("Некорректный ввод. Попробуйте ещё раз: ")
    finished = yesno == "нет"

