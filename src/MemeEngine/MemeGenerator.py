from PIL import Image, ImageFont, ImageDraw

class Meme:

    def __init__(self, output_dir):
        '''Insert docstring'''
        self.out_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:

        im = Image.open(img_path)

        im_width, im_height = im.size
        if im_width > width:
            scale_factor = width / im_width
            new_width = width
            new_height = int(im_height * scale_factor)
            im_resized = im.resize([new_width, new_height])
        else:
            im_resized = im

        font_type = ImageFont.truetype('FreeMono.ttf', 65)
        image_editable = ImageDraw.Draw(im_resized)
        image_editable.text(
            (im_resized.size[0]*0.1, im_resized.size[1]*0.9),
            text + ' ' + author,
            fill=(255, 255, 255),
            font=font_type
        )

        im.save(self.out_dir)

