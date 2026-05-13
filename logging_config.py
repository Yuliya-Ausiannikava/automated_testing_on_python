import logging


def get_logger(my_logger: str) -> logging.Logger:
    logger = logging.getLogger(my_logger)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)
    return logger
