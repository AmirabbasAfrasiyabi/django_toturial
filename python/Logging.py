# import logging
# #level
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')


# #filemode
# logging.basicConfig(filename='app.log', filemode='w')
# logging.warning('This will get logged to a file')


# #format
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This is a warning message')


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


## example 2

# import logging

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)


## example 3
import logging
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')