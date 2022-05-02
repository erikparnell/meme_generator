from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from typing import List
import docx


class DocxIngestor(IngestorInterface):
    '''Class for handling DOCX file types'''
    allowed_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
