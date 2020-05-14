from google.cloud import storage
import datetime


def rename_blob(bucket_name):
    """Copies a blob from one bucket to another with a new name."""
    time = datetime.datetime.now().strftime("%H%M%S")
    bucket_name = "YOUR-SOURCE-BUCKET"
    blob_name = "YOUR-SOURCE-BLOB-NAME"
    destination_bucket_name = "YOUR-TARGET-BUCKET"
    destination_blob_name = "YOUR TAGET-BLOB-NAME"
  

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )
