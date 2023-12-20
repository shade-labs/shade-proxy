from abc import ABC
from abc import abstractmethod


"""
Add more cloud providers using this API or remove unused ones
"""


class Provider(ABC):
    @abstractmethod
    def get_uid_from_token(self, token: str) -> str:
        pass

    @abstractmethod
    def create_signed_url(self, blob_name: str) -> str:
        pass
