import io
import os
import uuid
from pathlib import Path
from typing import List

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from shade import ShadeRemote

from proxy.__main__ import provider

shade_server = ShadeRemote(Path("/"), Path("/"), os.getenv("SHADE_ADDRESS"), int(os.getenv("SHADE_PORT")))

router = APIRouter(tags=["io"])


@router.get(
    '/search',
    summary="Search shade server for files."
)
async def search(query: str) -> List[str]:
    """
    Forward a shade search query
    """
    uid = provider.get_uid_from_token('token')
    # Secure folder search for only their folder by UID
    return shade_server.search.search(query=query, folder=f'/{uid}', recursive=True)


@router.get(
    '/preview',
    summary='Exchange a shade preview id for an image'
)
async def preview(preview_id: uuid.UUID):
    """
    Return a JPEG image response for a given preview id
    """
    # Get the Pillow image from your shade server
    image = shade_server.previews.get_preview(preview_id)

    # Convert the Pillow image to a byte stream
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    # Create a StreamingResponse
    return StreamingResponse(img_byte_arr, media_type="image/jpeg")
