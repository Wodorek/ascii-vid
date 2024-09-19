from PIL import Image


def process_frame(frame):
    img = Image.open(frame).convert('RGBA')

    pixels = img.getdata()

    print(pixels[1])
