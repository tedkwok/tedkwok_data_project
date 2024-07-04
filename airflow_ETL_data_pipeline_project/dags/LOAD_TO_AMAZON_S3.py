from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def load_to_s3(filename , key, bucket_name):
    hook = S3Hook("s3_connect")
    hook.load_file(filename = filename , key= key , bucket_name = bucket_name)