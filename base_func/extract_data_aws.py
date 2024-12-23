# code to extract documents from a s3 bucket in AWS

import boto3

def extract_documents_from_s3(bucket_name, prefix=''):
    s3 = boto3.client('s3')
    documents = []

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response.get('Contents', []):
        key = obj['Key']
        document = s3.get_object(Bucket=bucket_name, Key=key)
        content = document['Body'].read().decode('utf-8')
        documents.append(content)

    return documents

#
