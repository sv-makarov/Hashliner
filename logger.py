import logging  # модуль для ведения логов

# ------------- Настраиваем формат логирования  -------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    filename="hasher.log",
    encoding="utf-8",
)
