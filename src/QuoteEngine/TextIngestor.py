from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    '''insert docstring'''
    allowed_types = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path) as f:
            lines = f.readlines()

        for line in lines:
            parse = line.split('-')
            new_quote = QuoteModel(parse[0], parse[1])
            quotes.append(new_quote)

        return quotes
