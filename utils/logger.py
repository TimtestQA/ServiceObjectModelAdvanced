import logging
from logging.handlers import RotatingFileHandler

# Настраиваем логгер
logger = logging.getLogger('api_logger')  # Имя логгера
logger.setLevel(logging.DEBUG)  # Уровень логирования

# Хендлер для ротации логов
file_handler = RotatingFileHandler(
    'logs/api_requests.log',  # Имя файла
    maxBytes=5*1024*1024,  # Максимальный размер файла в байтах (5 МБ)
    backupCount=5  # Количество резервных копий
)
file_handler.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем хендлеры к логгеру
logger.addHandler(file_handler)

# Хендлер для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)