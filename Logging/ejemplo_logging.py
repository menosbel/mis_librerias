import logging
import datetime
from os import path
import glob



def init_logging():
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    if (logger.hasHandlers()):
        logger.handlers.clear()
    
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    
    file_name = create_file_name()
    
    file_handler = logging.FileHandler('Logs\\' + file_name)
    file_handler.setFormatter(formatter)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    

# Crear carpeta Logs en el directorio del script
def create_file_name():
    date = datetime.date.today()
    num = 0
    file_name = 'Log-' +  str(date) + '-' + str(num) + '.log'
    
    if path.exists('Logs\\' + file_name):
        newest = max(glob.iglob('Logs/*.log'), key=path.getctime)
        split = newest.replace('.', '-').split('-')
        num = int(split[4])
        num += 1
        
        file_name = 'Log-' + str(date) + '-' + str(num) + '.log'    
        
    return file_name


init_logging()


variable = "Hola"
logger.debug('Mensaje {}'.format(variable))
logger.info('Mensaje {}'.format(variable))
logger.exception('Mensaje {}'.format(variable))