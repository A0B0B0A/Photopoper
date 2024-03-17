from PIL import Image, ImageFilter


with Image.open('beer.jpg') as original:
    pic_gray= original.convert("L")
    pic_gray.save("black.jpg")
    pic_gray.show() 