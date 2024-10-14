import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('{asctime} - {levelname} - {msg}', style='{')

logger_DEBUG = logging.FileHandler('debug_info.log', encoding='UTF-8')
logger_DEBUG.setFormatter(formatter)
logger.addHandler(logger_DEBUG)

logger_WARNING = logging.FileHandler('warnings_errors.log', encoding='UTF-8')
logger_WARNING.setLevel(logging.WARNING)
logger_WARNING.setFormatter(formatter)
logger.addHandler(logger_WARNING)


logger.debug('Это дебаг')
logger.info('Это инфо')
logger.warning('Это предупреждение')
logger.error('Это ошибка')
logger.critical('Это критическая ошибка')


