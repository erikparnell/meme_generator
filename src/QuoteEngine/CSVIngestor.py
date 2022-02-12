from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from typing import List
import csv


class PDFIngestor(IngestorInterface):
    allowed_types = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        
        with open(path) as c:
            reader = csv.reader(c)
            next(reader)
            for row in reader:
                parse = row.split(',')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
            return quotes