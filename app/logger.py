import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

"""
    level: Niveau de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
"""
def setup_logging(level=logging.DEBUG):
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Handler fichier (rotation)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        mode="w",
        maxBytes=5_000_000,  # 5 MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Logger racine
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Évite les doublons
    root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
