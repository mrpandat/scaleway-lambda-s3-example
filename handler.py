import boto3
import os
from datetime import datetime, timedelta


def handle(event, context):
    SOURCE_BUCKET = 'backup-databases-fresh'
    DESTINATION_BUCKET = 'backup-databases-old'
        
    session = boto3.session.Session()
    ACCESS_KEY_ID = os.environ['aws_access_key_id']
    ACCESS_KEY = os.environ['aws_secret_access_key']

    s3_client = session.client(
        service_name='s3',
        region_name='fr-par',
        use_ssl=True,
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_KEY,
        endpoint_url='https://s3.fr-par.scw.cloud',
    )    
    
    # Create a reusable Paginator
    paginator = s3_client.get_paginator('list_objects_v2')
    
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket=SOURCE_BUCKET)
    print(page_iterator)

    # Loop through each object, looking for ones older than a given time period
    for page in page_iterator:
        for object in page['Contents']:
            if object['LastModified'] < datetime.now().astimezone() - timedelta(hours=1):   # <-- Change time period here
                print(f"Moving {object['Key']}")
        
                # Copy object
                s3_client.copy_object(
                    Bucket=DESTINATION_BUCKET,
                    Key=object['Key'],
                    CopySource={'Bucket':SOURCE_BUCKET, 'Key':object['Key']}
                )
    
                # Uncomment this to delete original object
                # s3_client.delete_object(Bucket=SOURCE_BUCKET, Key=object['Key'])
    return {
        "body": json.dumps({"message": "Hello"}),
        "statusCode": 200,
    }
