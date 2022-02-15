import random
import os
import requests
#from MemeEngine.MemeGenerator import Meme
from flask import Flask, render_template, abort, request
#from QuoteEngine import DocxIngestor
from MemeEngine import MemeGenerator
from QuoteEngine import Ingestor
from meme import generate_meme

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeGenerator.Meme('./tmp')  # or ./static ?


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv'
                  ]

    quotes = []

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
    
    return quotes, imgs


quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    meme = MemeGenerator.Meme('./static')
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')
    

@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    rand_num = random.randint(1, 100000)
    tmp = f'./tmp/meme{rand_num}.png'

    r = requests.get(image_url)

    with open(tmp, 'wb') as img:
        img.write(r.content)

    path = generate_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
