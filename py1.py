import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

font_path = 'resources/fonts/GreatVibes-Regular.ttf'
# certificate_path = 'resources/jc.png'
csv_path = 'resources/csvfiles/test.csv'

# Load font with freetype for better handling of diverse fonts
font = ImageFont.truetype(font_path, size=160)


def calculate_text_position(text, font, image_width, image_height):
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2
    return x, y


def create_certificate(name,pin,evname):

    global img, ev_name
    if evname == 1:
        ev_name='snl'
        img = Image.open('resources/certificates/snl.png')
    elif evname == 2:
        ev_name='jc'
        img = Image.open('resources/certificates/jc.png')
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size

    x, y = calculate_text_position(name, font, image_width, image_height)
    draw.text((x, y-110), text=name, fill=(0 ,0, 0), font=font)

    unique_id = str(hash(name))  # Example of adding a unique identifier
    save_path = os.path.join('pictures', f'{name}-{ev_name}-{pin}.png')
    img.save(save_path, quality=100)


df = pd.read_csv(csv_path)

for index, row in df.iterrows():
    name = row['name']
    pin = row['pin_no']
    print("Input the option number:")
    print("1.SnL - Snake And Ladders\n2.Jumbled Code")
    evname = int(input())
    create_certificate(name,pin,evname)
