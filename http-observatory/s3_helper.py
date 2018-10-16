import boto
import boto.s3
import os
import sys
import os.path


def send_to_s3(file_path):
    """
    Upload a file to a given s3 bucket
    """
    key_name = os.path.basename(file_path)

    param_store = AWSParameterstoreProvider()
    bucket_name = param_store.key('observatory-s3-bucket')

    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket_name, validate=False)
    key = boto.s3.key.Key(bucket)
    key.key = key_name
    key.set_contents_from_filename(file_path)

    key.set_acl('public-read')
    url = "https://s3.amazonaws.com/{}/{}".format(bucket.name, key.name)
    logging.info("Uploaded result file to URL: {}".format(url))
