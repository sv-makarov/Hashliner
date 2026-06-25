import logging  # модуль для ведения логов
import hashlib  # модуль для хеширования
import os  # модуль для работы с путями к файлу и каталогам
import csv  # модуль для ведения работы с csv файлами
from tkinter import *  # модули GUI
from tkinter import (
    filedialog,
    messagebox,
    simpledialog,
)
from tkinter import ttk  # модуль GUI


# ------------- Функция выбора исходного CSV файла, создания нового файла и хеширования значений  -------------
def hash_csv_file():
    logging.info("Начало работы с CSV файлом")

    def detect_encoding(file_path):
        logging.info("Запуск определения кодировки файла")
        """Автоматически определяет кодировку файла"""
        encodings = ["utf-8", "cp1251", "windows-1251", "koi8-r", "cp866"]
        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    f.read()
                return encoding
            except (UnicodeDecodeError, UnicodeError):
                continue
        return "utf-8"

    # Открывается окно выбора файла
    logging.info("Окно выбора файла")
    file_path = filedialog.askopenfilename(
        title="Выберите CSV файл",
        filetypes=[("CSV файлы", "*.csv"), ("Все файлы", "*.*")],
    )

    # если пользователь закрыл окно, то возвращаемся и ничего не делаем
    if not file_path:
        return

    try:
        # Определяем кодировку файла
        encoding = detect_encoding(file_path)

        # Спрашиваем пользователя о разделителе
        logging.info("Окно с вводом разделителя")
        delimiter = simpledialog.askstring(
            "Укажите разделитель в файле",
            "Введите символ-разделитель в исходном CSV файле:",
            initialvalue=";",
        )

        # Если пользователь нажал закрыл или не ввел ничего, то вовзращаемся на шаг раньше
        if not delimiter:
            return

        # пути к файлам, исходному и новому
        logging.info("Работа с путями файлов")
        folder = os.path.dirname(file_path)
        filename = "hash_" + os.path.basename(file_path)
        new_file_path = os.path.join(folder, filename)

        # Счетчики для статистики
        total_rows = 0
        total_cells = 0
        hashed_cells = 0
        empty_cells = 0

        # Открываем исходный и новый файл
        logging.info("Открытие исходного файла и создание нового файла")
        with open(file_path, "r", encoding=encoding) as infile, open(
            new_file_path, "w", encoding="utf-8", newline=""
        ) as outfile:

            # Создаем читатель и писатель с указанным разделителем ранее
            reader = csv.reader(infile, delimiter=delimiter)
            writer = csv.writer(outfile, delimiter=delimiter)

            # Обрабатываем каждую строку, хеширование данных
            logging.info("Построчная обработка и хеширование данных")
            for row in reader:
                total_rows += 1
                new_row = []
                for cell in row:
                    total_cells += 1
                    # Если ячейка не пустая, то хешируем ее, иначе оставляем пустой
                    if cell.strip():
                        hash_obj = hashlib.sha256(cell.strip().encode("utf-8"))
                        new_row.append(hash_obj.hexdigest())
                        hashed_cells += 1
                    else:
                        new_row.append("")
                        empty_cells += 1
                writer.writerow(new_row)

        # Логируем результат со статистикой
        logging.info(
            f"Успешно\n"
            f"Статистика обработки:\n"
            f"Обработано строк: {total_rows}\n"
            f"Обработано ячеек: {total_cells}\n"
            f"Захешировано ячеек: {hashed_cells}\n"
            f"Пустых ячеек: {empty_cells}\n"
            f"Использован разделитель: '{delimiter}'"
        )
        # выводим попап окно со статистикой
        messagebox.showinfo(
            "Готово!",
            f"Файл сохранен:\n{new_file_path}\n\n"
            f"Статистика обработки:\n"
            f"Обработано строк: {total_rows}\n"
            f"Обработано ячеек: {total_cells}\n"
            f"Захешировано ячеек: {hashed_cells}\n"
            f"Пустых ячеек: {empty_cells}\n"
            f"Использован разделитель: '{delimiter}'",
        )
    # # Отлавливаем ошибку, если она есть
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        messagebox.showerror("Ошибка", f"Ошибка: {e}")
