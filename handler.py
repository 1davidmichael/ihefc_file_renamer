import json
import boto3


def rename(event, context):

    s3_object_key = event[0]['s3']['object']['key']

    response = {
        "statusCode": 200,
        "body": json.dumps(s3_object_key)
    }

    return response
