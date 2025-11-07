import logging  # модуль для ведения логов
import hashlib  # модуль для хеширования
import os  # модуль для работы с путями к файлу и каталогам
from tkinter import *  # модули GUI
from tkinter import (
    filedialog,
    messagebox,
    simpledialog,
)
from tkinter import ttk  # модуль GUI


# ------------- Функция выбора исходного TXT файла, создания нового файла и хеширования строк  -------------
def hash_txt_file():
    logging.info("Начало работы с TXT файлом")

    def detect_encoding(file_path):
        logging.info("Запуск автоматического определения кодировки файла")
        """Автоматически определяет кодировку файла"""
        encodings = ["utf-8", "cp1251", "windows-1251", "koi8-r", "cp866"]
        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    f.read()
                return encoding
            except (UnicodeDecodeError, UnicodeError):
                continue
        return "utf-8"  # кодировка по умолчанию

    # Выбор файла
    logging.info("Диалоговое окно выбора txt файла")
    file_path = filedialog.askopenfilename(
        title="Выберите TXT файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )

    if not file_path:
        return

    try:

        logging.info("Работаем с путями txt файла")
        # Применяем кодировку
        encoding = detect_encoding(file_path)

        folder = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
        new_filename = "hash_" + filename
        new_file_path = os.path.join(folder, new_filename)

        # Счетчики
        total_lines = 0
        hashed_lines = 0
        empty_lines = 0

        logging.info("Открытие файла, хеширование, запись хеша в новый файл")
        with open(file_path, "r", encoding=encoding) as source_file, open(
            new_file_path, "w", encoding="utf-8"
        ) as hash_txt_file:

            for line in source_file:
                total_lines += 1
                clean_line = line.strip()

                if not clean_line:
                    empty_lines += 1
                    continue

                # Хешируем
                hash_hex = hashlib.sha256(clean_line.encode("utf-8")).hexdigest()
                hashed_lines += 1

                # Записываем хеш
                hash_txt_file.write(hash_hex + "\n")

        messagebox.showinfo(
            "Успешно!",
            f"Файл создан:\n{new_file_path}\n\n"
            f"Статистика обработки:\n"
            f"• Всего строк в файле: {total_lines}\n"
            f"• Успешно обработано: {hashed_lines}\n"
            f"• Пустых строк: {empty_lines}\n",
        )

        logging.info(
            f"Успешно\n"
            f"Статистика обработки:\n"
            f"• Всего строк в файле: {total_lines}\n"
            f"• Успешно обработано: {hashed_lines}\n"
            f"• Пустых строк: {empty_lines}\n",
        )

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")
