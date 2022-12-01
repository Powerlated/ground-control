import dearpygui.dearpygui as gui
from app import App
import logging

if __name__ == '__main__':
    logger = logging.getLogger('ground_control')
    logger.setLevel(logging.DEBUG)

    # Make logs be saved to a .csv file
    file_log_handler = logging.FileHandler('log.csv', 'w')
    file_log_handler.setLevel(logging.DEBUG)
    file_log_formatter = logging.Formatter('%(created)f,%(name)s,%(levelname)s,%(message)s')
    file_log_handler.setFormatter(file_log_formatter)
    logger.addHandler(file_log_handler)

    # Make logs be written to stdout
    stdout_log_handler = logging.StreamHandler()
    stdout_log_handler.setLevel(logging.DEBUG)
    stdout_log_formatter = logging.Formatter('[%(levelname)s] %(name)s: %(message)s')
    stdout_log_handler.setFormatter(stdout_log_formatter)
    logger.addHandler(stdout_log_handler)

    logger.info('Program started.')
    app = App()
    app.run()
    logger.info('Program stopped.')
    