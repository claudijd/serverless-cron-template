import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from awsparameterstoreprovider import AWSParameterstoreProvider


def run(event, context):
    param_store = AWSParameterstoreProvider()
    logging.error(param_store.key('test-parameter'))
