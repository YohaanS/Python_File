import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
datefmt="%m/%d/%Y %H:%M:%S")
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info("You can read this because of logging")
logger.debug("We will need to change some of this to make it more better")
logger.warning("Don't name your file the name of the thing you are importing")
logger.error("No error found")
logger.critical("if you don't put basicConfig the logging won't be organized and it will only put Warning, Error and Critical")
