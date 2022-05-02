INTRODUCTION
------------

The modules in this repository allow the user to generate custom or random
memes. The random meme function allows the user to enter the URL of the image,
the quote text, and the author name text, which then combines those items to
generate a meme which is outputted to the user. This is all achieved through
the users web browser using the Flask framework.

REQUIREMENTS
-------------

Ensure Python 3 is installed on the user's machine. Consult the
requirements.txt file. 

DETAILED INSTRUCTIONS
----------------------

After cloning the repository from Github using 'git clone', the user needs to
change to the source directory using 'cd ./src'. At this point the 'app.py'
file will be in the current directory. Start the program using
'python3 app.py'. If the correct permissions do not exist to execute the file,
first type 'chmod +x app.py'. Once the application is running the terminal
output will display some information as well as the local web address to load
the WebGUI from a web browser. With a web browser type the following in to the
address bar, "http://127.0.0.1:5000/". This will display a random meme
initially. Click "Random" to generate more random memes in the WebGUI.
Alternatively, click "Creator" to create a custom meme. Enter a URL of an image
file from the internet, for example, "https://upload.wikimedia.org/wikipedia/
commons/3/34/Art-portrait-collage_2.jpg". Enter a quote and an author name in
the respective fields. Then click "Create Meme!" to display a custom meme.

UNDER THE HOOD
---------------
The code is made of several components as follows:
- Meme Engine Module - Contains the "MemeGenerator" file which defines the
"meme" class, allowing the user to create meme class instances and make memes
using the "make_meme" method.
- Quote Engine Module - Contains an "Ingestor" class which interfaces with
specialized ingestor classes for various file types such as CSV, DOCX, PDF,
and TXT.
- Dog Quotes Files - A collection of different file types containing quotes.
- Dog Photo Files - Various random dog photos used for random meme generation.
- Web templates - Used to display a WebGUI in the browser and to interface with
Flask and python code.
- A "Meme" file - Essentially enables a command line version of the Flask
WebGUI, allowing the user to generate memes from the command line.
- A Flask "app" file - This is the main Flask application that enables the user
to generate memes through the WebGUI. It interfaces with all of the modules and
sub modules listed above to accomplish this.

