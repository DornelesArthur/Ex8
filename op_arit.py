from PIL import Image
from tkinter import messagebox

class ImageCalcArit():

    def addition(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        if (Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k] >255):
                            colors.append(255)
                        else:
                            colors.append(Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k])
                    
                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = Image1.getpixel((i,j)) + Image2.getpixel((i,j))
                    new_image.putpixel( (i,j), color)

        return new_image

    def subtraction(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        if (Image1.getpixel((i,j))[k] - Image2.getpixel((i,j))[k] < 0):
                            colors.append(0)
                        else:
                            colors.append(Image1.getpixel((i,j))[k] - Image2.getpixel((i,j))[k])
                    
                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = Image1.getpixel((i,j)) - Image2.getpixel((i,j))
                    new_image.putpixel( (i,j), color)

        return new_image

    def multiplication(self, Image1, val):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        if (Image1.getpixel((i,j))[k] * val > 255):
                            colors.append(255)
                        else:
                            colors.append(int(Image1.getpixel((i,j))[k] * val))

                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = int(Image1.getpixel((i,j)) * val)
                    new_image.putpixel( (i,j), color)
        return new_image

    def division(self, Image1, val):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        if (Image1.getpixel((i,j))[k] / val < 0):
                            colors.append(0)
                        else:
                            colors.append(int(Image1.getpixel((i,j))[k] / val))

                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = int(Image1.getpixel((i,j)) / val)
                    new_image.putpixel( (i,j), color)

        return new_image

    def mean(self, Image1, Image2):
        width, height = Image1.size
        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        colors.append((Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k]) * 0.5)

                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = (Image1.getpixel((i,j)) + Image2.getpixel((i,j))) * 0.5
                    new_image.putpixel( (i,j), color)

        return new_image

    def blending(self, Image1, Image2, val):
        width, height = Image1.size
        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    colors = []
                    for k in range (len(Image1.getpixel((0,0)))):
                        colors.append(int(val * Image1.getpixel((i,j))[k] + (1 - val) * Image2.getpixel((i,j))[k]))

                    new_image.putpixel( (i,j), tuple(colors))
                else:
                    color = int(val * Image1.getpixel((i,j)) + (1 - val) * Image2.getpixel((i,j)))
                    new_image.putpixel( (i,j), color)

        return new_image

    def image_to_gray(self, Image1):
        width, height = Image1.size

        new_image = Image.new("L", (width, height))
        for i in range(width):
            for j in range(height):
                if ( not isinstance(Image1.getpixel((0,0)), int)):
                    val = 0
                    for k in range (len(Image1.getpixel((0,0)))):
                        val = val + Image1.getpixel((i,j))[k]
                    val = val/len(Image1.getpixel((0,0)))
                    new_image.putpixel( (i,j), (int(val)))
                else:
                    return Image1
        return new_image
    
    def image_to_bin(self, Image1):
        if ( not isinstance(int, type(Image1.getpixel((0,0)))) ):
            Image1 = self.image_to_gray(Image1)
        width, height = Image1.size

        new_image = Image.new("1", (width, height))
        for i in range(width):
            for j in range(height):
                if (Image1.getpixel((i,j)) < 128):
                    new_image.putpixel( (i,j), 0)
                else:
                    new_image.putpixel( (i,j), 1)
        return new_image