import boto3
import sys
import os

#======== Set up zone ================#
bucket_name = 'writerside-demo-docs'
yandex_s3_endpoint = "https://storage.yandexcloud.net"

#=====================================#

def get_s3_session(access_key_id, secret_access_key):
    session = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name="ru-central1",
    )
    s3 = session.client("s3", endpoint_url=yandex_s3_endpoint)
    return s3

def clean_s3_bucket(s3_session, tag):
    prefix = f'versions/{tag}/'
    paginator = s3_session.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    delete_keys = []
    for page in pages:
        if 'Contents' in page:
            for obj in page['Contents']:
                delete_keys.append({'Key': obj['Key']})

    if delete_keys:
        s3_session.delete_objects(Bucket=bucket_name, Delete={'Objects': delete_keys})
        print(f"Все объекты под префиксом '{prefix}' удалены из бакета '{bucket_name}'.")
    else:
        print(f"Нет объектов для удаления под префиксом '{prefix}' в бакете '{bucket_name}'.")

def upload_doc_s3(s3_session, bucket_name, folder_path, tag):
    prefix = f'versions/{tag}/'
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, folder_path)
            s3_key = os.path.join(prefix, relative_path).replace('\\', '/')
            s3_session.upload_file(local_path, bucket_name, s3_key)
            print(f"Загружен {local_path} в s3://{bucket_name}/{s3_key}")
    print("Все файлы успешно загружены.")

def run(documentation_folder, access_key_id, secret_access_key, current_tag):
    s3_connect = get_s3_session(access_key_id=access_key_id, secret_access_key=secret_access_key)
    clean_s3_bucket(s3_session=s3_connect, tag=current_tag)
    upload_doc_s3(s3_session=s3_connect, bucket_name=bucket_name, folder_path=documentation_folder, tag=current_tag)

if __name__ == "__main__":
    run(
        documentation_folder=sys.argv[1],
        access_key_id=sys.argv[2],
        secret_access_key=sys.argv[3],
        current_tag=sys.argv[4]
    )