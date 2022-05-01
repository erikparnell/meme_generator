from QuoteEngine import DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor
from .IngestorInterface import IngestorInterface

from .Quote import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    '''insert docstring'''

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
