from abc import ABC, abstractmethod
from typing import List

from .Quote import QuoteModel


class IngestorInterface(ABC):
    '''insert docstring'''
    allowed_types = []  # 'pdf', 'docx', 'txt', 'csv'

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.split('.')[-1] in cls.allowed_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
