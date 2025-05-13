import logging


def get_logger(name: str) -> logging.Logger:
    # Инициализация логгера
    logger = logging.getLogger(name)
    # Устанавливаем уровень логирования DEBUG для логгера
    # Чтобы все сообщения уровня DEBUG и выше были записаны в лог файл
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в консоль
    handler = logging.StreamHandler()
    # Устанавливаем уровень логирования DEBUG для обработчика
    # Чтобы он обрабатывал все сообщения уровня DEBUG и выше
    handler.setLevel(logging.DEBUG)

    # Задаем форматирование лог-сообщений: время, имя модуля, логгер и само сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    # Возвращаем настроенный логгер
    return logger