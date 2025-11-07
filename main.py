from hash_txt import hash_txt_file  # импорт функции работы с txt файлом
from hash_csv import hash_csv_file  # импорт функции работы с csv файлом
import os  # модуль для работы с путями к файлу и каталогам
from tkinter import *  # модули GUI
from tkinter import (
    filedialog,
    messagebox,
    simpledialog,
)
from tkinter import ttk  # модуль GUI


# ------------- Интерфейс программы -------------

window = Tk()
window.title("HashLiner - построчное хеширование TXT и CSV файлов (SHA256)")
window.geometry("560x290")

# создаём вкладки (объект Notebook)
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

# вкладка 1, Хеширование TXT файла
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Работа с TXT файлами")

# вкладка 2, Хеширование CSV файла
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Работа с CSV файлами")

# вкладка 3, О программе
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="О программе")

# Элементы на Вкладке 1, Текст над кнопкой
label = ttk.Label(
    tab1,
    text="Как работает программа:\n1. Выберите исходный txt файл, данные из которого нужно хешировать.\n2. Укажите используемый разделитель в исходном файле.\n3 Программа читает выбранный файл построчно, хеширует каждую строку алгоритмом SHA256 и полученный результат записывает в новый файл.\n4. Новый файл автоматически создаётся с именем hash_имяфайла.txt в той же папке, где находится исходный.\n5. После завершения появляется сообщение о результате работы.",
    wraplength=500,
)
label.grid(column=0, row=0, sticky="w")

# Элементы на Вкладке 1, Кнопка для выбора и хеширования файла
button = ttk.Button(
    tab1,
    text="Выбрать txt файл и хешировать данные",
    command=hash_txt_file,
)
button.grid(column=0, row=1, sticky="w")

# Элементы на Вкладке 2, Текст над кнопкой
label2 = ttk.Label(
    tab2,
    text="Как работает программа:\n1. Выберите исходный csv файл, данные из которого нужно хешировать.\n2. Укажите используемый разделитиль в исходном файле.\n3. Программа читает выбранный файл и хеширует каждое значение (ячейку) алгоритмом SHA256 и полученный результат записывает в новый файл. Если значение пустое, то оно остается пустым и не хешируется. Структура файла остается без изменений.\n4. Новый файл автоматически создаётся с именем hash_имяфайла.csv в той же папке, где находится исходный.\n5. После завершения появляется сообщение о результате работы.",
    wraplength=500,
)
label2.grid(column=0, row=0, sticky="w")

# Элементы на Вкладке 2, Кнопка для выбора и хеширования файла
button2 = ttk.Button(
    tab2,
    text="Выбрать csv файл и хешировать данные",
    command=hash_csv_file,
)
button2.grid(column=0, row=1, sticky="w")


# Элементы на Вкладке 3, О программе
label3 = ttk.Label(
    tab3,
    text="Программа хеширует данные в txt и csv файлах. Алгоритм хеширования - SHA256. Программа разработана на языке Python, для создание хешей используется библиотека Hashlib, графический интерфейс реализован с помощью библиотеки Tkinter. EXE-файл подготовлен с помощью PyInstaller.\n\n HashLiner.\n MIT License. \n\n Автор: Сергей Макаров. \n Сайт: sv-makarov.ru",
    wraplength=500,
)
label3.grid(column=0, row=0, sticky="w")


# Запуск главного цикла программы
window.mainloop()
