import datetime
import logging
import requests  # this is an example of an import

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    status_code = requests.get('https://mozilla.org/').status_code

    logger.info("Your cron function " + name + " ran at " + str(current_time))
    logger.info("Status code returned by mozilla.org: " + str(status_code))
