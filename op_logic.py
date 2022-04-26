from PIL import Image
import math

class ImageCalcLogic():
    
    def image_and(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append(Image1.getpixel((i,j))[k] & Image2.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def image_or(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append(Image1.getpixel((i,j))[k] | Image2.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def image_xor(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append(Image1.getpixel((i,j))[k] ^ Image2.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def image_not(self, Image1):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        max = 2**len(bin(Image1.getpixel((0,0))[0]))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append(max - Image1.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image
