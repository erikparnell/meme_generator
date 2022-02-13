import subprocess
from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import TextIngestor
from .Quote import QuoteModel


class PDFIngestor(IngestorInterface):
    '''insert docstring'''
    allowed_types = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        subprocess.run(["pdftotext", path])
        base = '.' + path.split('.')[1]
        new_path = base + '.txt'
        return TextIngestor.TextIngestor.parse(new_path)
