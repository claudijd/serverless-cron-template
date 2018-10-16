import boto3
import base64
from botocore.exceptions import ClientError


class SecretManager:
    def __init__(self, region_name):
        self.region_name = region_name

    def get(self, secret_name):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise e
        else:
            if 'SecretString' in get_secret_value_response:
                return get_secret_value_response['SecretString']
            else:
                return base64.b64decode(
                    get_secret_value_response['SecretBinary'])
