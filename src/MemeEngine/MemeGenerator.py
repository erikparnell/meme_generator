from PIL import Image, ImageFont, ImageDraw
import random


class Meme:

    def __init__(self, output_dir):
        '''Insert docstring'''
        self.out_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        '''Insert docstring'''
        im = Image.open(img_path)

        im_width, im_height = im.size
        if im_width > width:
            scale_factor = width / im_width
            new_width = width
            new_height = int(im_height * scale_factor)
            im_resized = im.resize([new_width, new_height])
        else:
            im_resized = im

        font_type = ImageFont.truetype('FreeMono.ttf', 25)
        image_editable = ImageDraw.Draw(im_resized)
        image_editable.text(
            (
                im_resized.size[0]*random.uniform(0.05, 0.1),
                im_resized.size[1]*random.uniform(0.3, 0.9)
            ),
            text + '\n' + '-' + author,
            fill=(255, 255, 255),
            font=font_type
        )
        
        im.save(self.out_dir + '/meme.png')  # need to see if filename needs to be specified in these lines too

        return self.out_dir
