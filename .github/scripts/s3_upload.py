import boto3
import os
from os import path
import zipfile

#======== Set up zone ================#
bucket_name = 'writerside-demo-docs'
yandex_s3_endpoint = "https://storage.yandexcloud.net"

#=====================================#

def unzip_file(zip_path, extract_to):
    
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Файлы извлечены в: {extract_to}")


def get_s3_session(access_key_id, secret_access_key):

    session = boto3.session.Session()
    session = boto3.Session(
        aws_access_key_id=(access_key_id),
        aws_secret_access_key=(secret_access_key),
        region_name="ru-central1",
    )

    s3 = session.client("s3", endpoint_url=yandex_s3_endpoint)
    return s3


def clean_s3_bucket(s3_session):
    
    # Получаем список всех объектов в бакете
    objects = s3_session.list_objects_v2(Bucket=bucket_name)

    # Проверяем, есть ли объекты для удаления
    if 'Contents' in objects:
        # Создаем список ключей объектов для удаления
        delete_keys = {'Objects': [{'Key': obj['Key']} for obj in objects['Contents']]}
        
        # Удаляем объекты
        s3_session.delete_objects(Bucket=bucket_name, Delete=delete_keys)
        print(f"Все объекты удалены из бакета '{bucket_name}'.")
    else:
        print(f"Бакет '{bucket_name}' уже пуст.")

def upload_doc_s3(s3_session, bucket_name, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Полный путь к файлу
            local_path = os.path.join(root, file)
            
            # Относительный путь для ключа в S3
            relative_path = os.path.relpath(local_path, folder_path)
            # Преобразуем пути для S3
            s3_key = relative_path.replace('\\', '/')
            
            # Загружаем файл в S3
            s3_session.upload_file(local_path, bucket_name, s3_key)
            print(f"Загружен {local_path} в s3://{bucket_name}/{s3_key}")
    print("Все файлы успешно загружены.")

def run(zip_archive_path, folder_to_unzip, access_key_id, secret_access_key):
    unzip_file(zip_path = zip_archive_path, extract_to=folder_to_unzip)
    s3_connect = get_s3_session(access_key_id=access_key_id, secret_access_key = secret_access_key)
    clean_s3_bucket(s3_session=s3_connect)
    upload_doc_s3(s3_session=s3_connect, bucket_name=bucket_name, folder_path=folder_to_unzip)

if __name__ == "__main__":
    run(zip_archive_path=os.argv[1], 
        folder_to_unzip=os.argv[2], 
        access_key_id = os.argv[3], 
        secret_access_key = os.argv[4])

    

