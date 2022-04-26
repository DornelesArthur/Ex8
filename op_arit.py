from PIL import Image
from tkinter import messagebox

class ImageCalcArit():
    max_red = 0
    min_red = 255
    max_green = 0
    min_green = 255
    max_blue = 0
    min_blue = 255

    def addition(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    if (Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k] >255):
                        colors.append(255)
                    else:
                        colors.append(Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def subtraction(self, Image1, Image2):
        width, height = Image1.size

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    if (Image1.getpixel((i,j))[k] - Image2.getpixel((i,j))[k] < 0):
                        colors.append(0)
                    else:
                        colors.append(Image1.getpixel((i,j))[k] - Image2.getpixel((i,j))[k])
                
                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def multiplication(self, Image1, val):
        width, height = Image1.size
        self.max_red = 0
        self.min_red = 255
        self.max_green = 0
        self.min_green = 255
        self.max_blue = 0
        self.min_blue = 255

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    if (Image1.getpixel((i,j))[k] * val > 255):
                        colors.append(255)
                    else:
                        colors.append(int(Image1.getpixel((i,j))[k] * val))

                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def division(self, Image1, val):
        width, height = Image1.size
        self.max_red = 0
        self.min_red = 255
        self.max_green = 0
        self.min_green = 255
        self.max_blue = 0
        self.min_blue = 255

        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    if (Image1.getpixel((i,j))[k] / val < 0):
                        colors.append(0)
                    else:
                        colors.append(int(Image1.getpixel((i,j))[k] / val))

                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def mean(self, Image1, Image2):
        width, height = Image1.size
        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append((Image1.getpixel((i,j))[k] + Image2.getpixel((i,j))[k]) * 0.5)

                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def blending(self, Image1, Image2, val):
        width, height = Image1.size
        new_image = Image.new(Image1.mode, (width, height))
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image1.getpixel((0,0)))):
                    colors.append(int(val * Image1.getpixel((i,j))[k] + (1 - val) * Image2.getpixel((i,j))[k]))

                new_image.putpixel( (i,j), tuple(colors))
        return new_image

    def normalize(self, Image):
        width, height = Image.size
        for i in range(width):
            for j in range(height):
                colors = []
                for k in range (len(Image.getpixel((0,0)))):
                    colors.append(255.0/(self.max_red - self.min_red) * (Image.getpixel((i,j))[k] - self.min_red))

                Image.putpixel( (i,j), tuple(colors))
        return Image