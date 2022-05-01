import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeGenerator
from QuoteEngine import Ingestor
from meme import generate_meme

app = Flask(__name__)


def setup():
    """ Load all resources """

    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
                  ]

    quotes = []

    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

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

    image_url = request.form['image_url']
    print(image_url)
    body = request.form['body']
    author = request.form['author']

    rand_num = random.randint(1, 100000)
    print(rand_num)
    tmp = f'./static/meme{rand_num}.png'
    print(tmp)

    r = requests.get(image_url)

    with open(tmp, 'wb') as img:
        img.write(r.content)

    path = generate_meme(tmp, body, author)
    print(path)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
