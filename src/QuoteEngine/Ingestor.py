import IngestorInterface
import DocxIngestor
import CSVIngestor
import PDFIngestor
import TextIngestor
from .Quote import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    '''https://knowledge.udacity.com/questions/559464'''
    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
