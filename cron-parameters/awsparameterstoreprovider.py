import boto3
import json
import os
from jose import jwk


class AWSParameterstoreProvider(object):
    """Support loading secure strings from AWS parameter store."""

    def __init__(self):
        # self.config = common.get_config()
        # self.region_name = self.config(
        #     'secret_manager_ssm_region', namespace='cis', default='us-west-2')
        self.region_name = 'us-east-1'
        self.boto_session = boto3.session.Session(region_name=self.region_name)
        self.ssm_client = self.boto_session.client('ssm')

    def key(self, key_name):
        # ssm_namespace = self.config(
        #     'secret_manager_ssm_path', namespace='cis', default='/iam')
        ssm_response = self.ssm_client.get_parameter(
            #Name='{}/{}'.format(ssm_namespace, key_name),
            Name='{}'.format(key_name),
            WithDecryption=True
        )

        result = ssm_response.get('Parameter')
        try:
            key_dict = json.loads(result.get('Value'))
            key_construct = jwk.construct(key_dict, 'RS256')
        except json.decoder.JSONDecodeError:
            key_construct = jwk.construct(result.get('Value'), 'RS256')
        return key_construct
