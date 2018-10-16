import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from secretmanager import SecretManager


def run(event, context):

    # Example: Retrieve a secret from secretmanager
    sm = SecretManager('us-east-1')
    logging.error(sm.get("serverless-cron-jabbas-secret-dev"))
