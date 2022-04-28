import os
import random
import argparse
from MemeEngine import MemeGenerator
from QuoteEngine import Quote, Ingestor

# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote """
    #img = None
    #quote = None
    print(path, body, author)
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path  # ? need index [0]?
        print(img)
    if body is None:
        print("thinks body is none")
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            print("thinks author is none")
            raise Exception('Author Required if Body is Used')
        quote = Quote.QuoteModel(body, author) #missing last else statement for when author and body is good
        print(quote)
            
    print("got here")
    meme = MemeGenerator.Meme('./static')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", nargs="?", const=None, 
                    help="path to an image file")
    parser.add_argument("-b", "--body", nargs="?", const=None, 
                    help="quote body to add to the image")                    
    parser.add_argument("-a", "--author", nargs="?", const=None, 
                    help="quote author to add to the image")                    
    args = parser.parse_args()
    print(args)
    generate_meme(args.path, args.body, args.author)
