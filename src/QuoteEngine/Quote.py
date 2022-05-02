class QuoteModel:
    '''Class for quotes which are made of text and author name strings'''
    def __init__(self, body: str, author: str):
        "Initialize quote"
        self.body = body
        self.author = author

    def __repr__(self):
        "Displays quote for printing in terminal"
        return f'<{self.body}, {self.author}>'
