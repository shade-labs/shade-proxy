import datetime
import os
from datetime import datetime
from datetime import timedelta

from google.cloud import storage

from proxy.providers.abc_provider import Provider


class GCS(Provider):
    def __init__(self):
        # Not that you need anything here
        pass

    def get_uid_from_token(self, token: str) -> str:
        return 'example-uid'

    def create_signed_url(self, blob_name: str) -> str:
        """
        Create a signed URL for uploading a file to the server at f`{uid}/{uuid.uuid4()}`
        """
        storage_client = storage.Client()
        bucket = storage_client.bucket(os.getenv('CLOUD_BUCKET'))
        blob = bucket.blob(blob_name)

        url = blob.generate_signed_url(
            version='v4',
            expiration=datetime.utcnow() + timedelta(minutes=15),
        )
        return url

