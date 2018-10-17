import datetime
import logging

from s3_helper import send_to_s3

from observatory_scanner import ObservatoryScanner
from randomizer import Randomizer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    # Test out S3 upload capability
    url = 'https://raw.githubusercontent.com/mozilla/http-observatory-dashboard/master/httpobsdashboard/conf/sites.json'
    randomizer = Randomizer(url)
    scanner = ObservatoryScanner()
    hostname = randomizer.next()
    scan_result = scanner.scan(hostname)
    logger.info(scan_result)
    send_to_s3(hostname, scan_result)
