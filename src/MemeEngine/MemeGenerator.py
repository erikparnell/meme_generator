from PIL import Image, ImageFont, ImageDraw
import random


class Meme:

    def __init__(self, output_dir):
        '''Initialize a meme'''
        self.out_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        '''
        Method that "makes" the meme and outputs the final path directory

        Parameters:
        img_path (string): The file path of the image to be memed
        text (string): The text body of the quote
        author (string): The name of the author of the quote
        width (int): The integer value in pixels to not exceed image width

        Returns:
        The final output directory path of the meme
        '''
        im = Image.open(img_path)

        im_width, im_height = im.size
        if im_width > width:
            scale_factor = width / im_width
            new_width = width
            new_height = int(im_height * scale_factor)
            im_resized = im.resize([new_width, new_height])
        else:
            im_resized = im

        font_type = ImageFont.truetype('arial.ttf', 25)
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
        random_num = str(random.randint(0, 100000000))
        final_out_dir = self.out_dir + '/meme_' + random_num + '.png'
        im_resized.save(final_out_dir)
        return final_out_dir
