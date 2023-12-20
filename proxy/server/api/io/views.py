import uuid

from fastapi import APIRouter

from proxy.__main__ import provider

router = APIRouter(tags=["io"])


# convert colorspace route is under convert module
@router.post(
    '/file',
    summary="Create signed url for uploading a file to the storage bucket ."
)
async def upload() -> str:
    """
    Return a signed URL for uploading a file to the server at f`{uid}/{uuid.uuid4()}`
    """
    uid = provider.get_uid_from_token("token")

    return provider.create_signed_url(f"{uid}/{uuid.uuid4()}")

