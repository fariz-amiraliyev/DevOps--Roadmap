import logging

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
print("Ran entire script")


import logging

logging.basicConfig(filemode="w", filename="example.log", level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print("Ran entire script")


# Defining Log Formatters
import logging
format_string = "%(asctime)s [%(levelname)s] - %(filename)s : %(message)s"


logging.basicConfig(
    filemode="w", filename="example.log", format=format_string, level=logging.DEBUG
)

logging.debug("Debug message %s %s", "a", 1)
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print("Ran entire script")


#Using Multiple Log Handlers
import logging
import sys

format_string = "%(asctime)s [%(levelname)s] - %(filename)s : %(message)s"

# logging.basicConfig(
#     filemode="w", filename="example.log", format=format_string, level=logging.DEBUG
# )

logger = logging.getLogger()  # get the `root` logger

file_handler = logging.FileHandler(filename="example.log", mode="w")
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

logging.debug("Debug message %s %s", "a", 1)
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print("Ran entire script")

# In addition to customizing our loggers with handlers, we can also create Formatter
#  objects and use the logging.Handler.setFormatter method.
import logging
import sys

format_string = "%(asctime)s [%(levelname)s] - %(filename)s : %(message)s"

# logging.basicConfig(
#     filemode="w", filename="example.log", format=format_string, level=logging.DEBUG
# )

logger = logging.getLogger()  # get the `root` logger

formatter = logging.Formatter(format_string)

file_handler = logging.FileHandler(filename="example.log", mode="w")
file_handler.setFormatter(formatter)

stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

logging.debug("Debug message %s %s", "a", 1)
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print("Ran entire script")
