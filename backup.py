import logging
import boto3
from botocore.exceptions import ClientError
from time import time, ctime, sleep
import os
import sys
import shutil

def upload_file(file_name, bucket, secret, object_name=None):
    if object_name is None:
        object_name = file_name
    access_id = 'AKIAJMMPMLN4OMOSA7SQ'
    s3_client = boto3.client('s3', aws_access_key_id=access_id, aws_secret_access_key=secret, region_name='us-east-1')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def world_zip():
    t = time()
    time_stamp = ctime(t)
    path_name = 'world/'
    zip_name = 'world_' + str(t)
    shutil.make_archive(zip_name, 'zip', path_name)
    return zip_name + '.zip'
            
def main():
    # Backup every other day
    mult = 60 * 60 * 24 * 2
    
    secret = sys.argv[1]
    while(True):
        file_name = world_zip()
        upload_file(file_name=file_name, bucket='jcpackv2adventure', secret=secret)
        os.remove(file_name)
        sleep(mult)



if __name__ == "__main__":
    main()
