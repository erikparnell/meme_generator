from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    '''Class for handling CSV file types'''
    allowed_types = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path) as c:
            pd_csv = pd.read_csv(path, header=1, sep=';')
            for each in pd_csv:
                parse = each.split(',')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
            return quotes
