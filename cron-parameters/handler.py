import datetime
import logging
from awsparameterstoreprovider import AWSParameterstoreProvider


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    param_store = AWSParameterstoreProvider()
    logging.info(param_store.key('test-parameter'))
