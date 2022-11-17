from logging import getLogger, StreamHandler, DEBUG, Formatter


logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler()
format = Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(format)
logger.addHandler(handler)

logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')
