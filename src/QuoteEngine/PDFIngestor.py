import subprocess
from typing import List
from .IngestorInterface import IngestorInterface
import TextIngestor
from .Quote import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_types = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        try:
            subprocess.run('pdftotext ' + path)
            base = path.split('.')[0]
            new_path = base + '.txt'
            return TextIngestor.parse(new_path)
        except:
            print('Issue with pdftotext')
            quit()
        