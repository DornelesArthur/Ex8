from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from op_arit import ImageCalcArit
from op_logic import ImageCalcLogic
import time

class App:
    window = Tk()
    FONT = "Yu Gothic"
    width = 1280
    height = 540
    f_types = [('Jpg Files', '*.jpg')]
    canvas = None
    img1 = None
    img2 = None
    result_img = None
    img1_TK = None
    img2_TK = None
    LogicCalculator = ImageCalcLogic()
    ArithmeticCalculator = ImageCalcArit()
    modify_error = "Sem imagem para modificar!"
    save_error = "Sem imagem para salvar!"
    upload_error = "Erro ao enviar imagem!"
    number_error = "Input tem que ser um número!"
    size_mode_error = "Imagens de tamanhos ou tipos diferentes!"
    dark_color = "#D7D7D7"
    light_color = "#393939"
    multiply_val = StringVar()
    division_val = StringVar()
    blending_val = StringVar()
    

    def __init__(self) -> None:
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.configure(bg = self.dark_color)
        self.window.title("Operadores Aritméticas e Lógicas em Imagens")
        self.canvas = Canvas(
            self.window,
            bg = self.dark_color,
            height = self.height,
            width = self.width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.run()

    def UploadImage2(self):
        filename = filedialog.askopenfilename(filetypes=self.f_types)
        self.img2=Image.open(filename)
        self.img2_TK = self.img2.resize((300, 300), Image.ANTIALIAS)
        self.img2_TK = ImageTk.PhotoImage(self.img2_TK)
        

        b2 = Button(self.window,image=self.img2_TK) 
        b2.place(x=360, y=120)

    def UploadImage1(self):
        filename = filedialog.askopenfilename(filetypes=self.f_types)
        self.img1 = Image.open(filename)
        self.img1_TK = self.img1.resize((300, 300), Image.ANTIALIAS)
        self.img1_TK = ImageTk.PhotoImage(self.img1_TK)

        b1 = Button(self.window,image=self.img1_TK)
        b1.place(x=20, y=120)

    def SaveImage(self):
        if (self.result_img != None):
            self.result_img.save("result.jpg")
        else:
            messagebox.showerror("Error", self.save_error)

    def addition(self):
        if (self.img1.size == self.img2 and self.img1.mode == self.img2.mode):
            if (self.img1 != None and self.img2 != None):
                self.result_img = self.ArithmeticCalculator.addition(self.img1,self.img2)
                self.ShowResultImage()
            else:
                messagebox.showerror("Error", self.modify_error)
        else:
            messagebox.showerror("Error", self.size_mode_error)

    def subtraction(self):
        if (self.img1.size == self.img2 and self.img1.mode == self.img2.mode):
            if (self.img1 != None and self.img2 != None):
                self.result_img = self.ArithmeticCalculator.subtraction(self.img1,self.img2)
                self.ShowResultImage()
            else:
                messagebox.showerror("Error", self.modify_error)
        else:
            messagebox.showerror("Error", self.size_mode_error)

    def multiplication(self):
        try:
            val = float(self.multiply_val.get())
            if (self.img1 != None and val != 0):
                self.result_img = self.ArithmeticCalculator.multiplication(self.img1,val)
                self.ShowResultImage()
            else:
                messagebox.showerror("Error", self.modify_error)
        except ValueError as e:
            messagebox.showerror("Error", self.number_error)
        

    def division(self):
        try:
            val = float(self.division_val.get())
            if (self.img1 != None and val != 0):
                self.result_img = self.ArithmeticCalculator.division(self.img1,val)
                self.ShowResultImage()
            else:
                messagebox.showerror("Error", self.modify_error)
        except ValueError as e:
            messagebox.showerror("Error", self.number_error)
        

    def mean(self):
        if (self.img1.size == self.img2 and self.img1.mode == self.img2.mode):
            if (self.img1 != None and self.img2 != None):
                self.result_img = self.ArithmeticCalculator.mean(self.img1,self.img2)
                self.ShowResultImage()
            else:
                messagebox.showerror("Error", self.modify_error)
        else:
            messagebox.showerror("Error", self.size_mode_error)

    def blending(self):
        if (self.img1.size == self.img2 and self.img1.mode == self.img2.mode):
            try:
                val = float(self.blending_val.get())
                if (self.img1 != None and self.img2 != None and val != 0):
                    self.result_img = self.ArithmeticCalculator.blending(self.img1, self.img2,val)
                    self.ShowResultImage()
                else:
                    messagebox.showerror("Error", self.modify_error)
            except ValueError as e:
                messagebox.showerror("Error", self.number_error)
        else:
            messagebox.showerror("Error", self.size_mode_error)

    def image_and(self):
        if (self.img1 != None and self.img2 != None):
            self.result_img = self.LogicCalculator.image_and(self.img1,self.img2)
            self.ShowResultImage()
        else:
            messagebox.showerror("Error", self.modify_error)

    def image_or(self):
        if (self.img1 != None and self.img2 != None):
            self.result_img = self.LogicCalculator.image_or(self.img1,self.img2)
            self.ShowResultImage()
        else:
            messagebox.showerror("Error", self.modify_error)

    def image_xor(self):
        if (self.img1 != None and self.img2 != None):
            self.result_img = self.LogicCalculator.image_xor(self.img1,self.img2)
            self.ShowResultImage()
        else:
            messagebox.showerror("Error", self.modify_error)

    def image_not(self):
        if (self.img1 != None):
            self.result_img = self.LogicCalculator.image_not(self.img1)
            self.ShowResultImage()
        else:
            messagebox.showerror("Error", self.modify_error)

    def ShowResultImage(self):
        self.result_img.show()
        result_img_TK = self.result_img.resize((300, 300), Image.ANTIALIAS)
        result_img_TK = ImageTk.PhotoImage(result_img_TK)
        b1 = Button(self.window,image=result_img_TK)
        b1.place(x=960, y=120)

    def run(self):
        self.canvas.place(x = 0, y = 0)

        self.canvas.create_rectangle(0, 0, self.width, 70,
            outline=self.light_color, fill=self.light_color)

        self.canvas.create_rectangle(20, 120, 320, 420,
            outline=self.light_color, fill=self.light_color)

        self.canvas.create_rectangle(360, 120, 660, 420,
            outline=self.light_color, fill=self.light_color)
        
        self.canvas.create_rectangle(960, 120, 1260, 420,
            outline=self.light_color, fill=self.light_color)

        self.canvas.create_line(20, 500, 1240, 500, width=2, fill=self.light_color)

        up1Button = Button(self.window, text="Carregar Imagem 1", width=26, command=self.UploadImage1, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 14), activebackground=self.dark_color, activeforeground=self.light_color)
        up1Button.place(x=20, y=440)

        up2Button = Button(self.window, text="Carregar Imagem 2", width=26, command=self.UploadImage2, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 14), activebackground=self.dark_color, activeforeground=self.light_color)
        up2Button.place(x=360, y=440)

        saveButton = Button(self.window, text="Salvar Imagem", width=26, command=self.SaveImage, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 14), activebackground=self.dark_color, activeforeground=self.light_color)
        saveButton.place(x=960, y=440)

        additionButton = Button(self.window, text="Adição", width=12, command=self.addition, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        additionButton.place(x=700, y=120)

        subtractionButton = Button(self.window, text="Subtração", width=12, command=self.subtraction, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        subtractionButton.place(x=700, y=160)

        multiplicationButton = Button(self.window, text="Multiplicação", width=12, command=self.multiplication, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        multiplicationButton.place(x=700, y=200)

        divisionButton = Button(self.window, text="Divisão", width=12, command=self.division, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        divisionButton.place(x=700, y=240)

        meanButton = Button(self.window, text="Média", width=12, command=self.mean, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        meanButton.place(x=700, y=280)

        blendingButton = Button(self.window, text="Blending", width=12, command=self.blending, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        blendingButton.place(x=700, y=320)

        image_and_Button = Button(self.window, text="AND", width=12, command=self.image_and, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        image_and_Button.place(x=700, y=410)

        image_or_Button = Button(self.window, text="OR", width=12, command=self.image_or, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        image_or_Button.place(x=820, y=410)

        image_xor_Button = Button(self.window, text="XOR", width=12, command=self.image_xor, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        image_xor_Button.place(x=700, y=450)

        image_not_Button = Button(self.window, text="NOT", width=12, command=self.image_not, fg=self.dark_color, bg=self.light_color, font=(self.FONT, 10), activebackground=self.dark_color, activeforeground=self.light_color)
        image_not_Button.place(x=820, y=450)

        multiply_input = Entry(self.window, textvariable=self.multiply_val, bg="#CBC9C9", fg="#393939", font=(self.FONT, 12)).place(x=820, y=200, width=105,height=30)

        division_input = Entry(self.window, textvariable=self.division_val, bg="#CBC9C9", fg="#393939", font=(self.FONT, 12)).place(x=820, y=240, width=105,height=30)

        blending_input = Entry(self.window, textvariable=self.blending_val, bg="#CBC9C9", fg="#393939", font=(self.FONT, 12)).place(x=820, y=320, width=105,height=30)

        self.canvas.create_text(
            640, 35.0,
            text = "Operadores Aritméticas e Lógicas em Imagens",
            fill = self.dark_color,
            font = (self.FONT, int(26.0)))

        self.canvas.create_text(
            65, 100,
            text = "Imagem 1:",
            fill = self.light_color,
            font = (self.FONT, int(14.0)))

        self.canvas.create_text(
            405, 100,
            text = "Imagem 2:",
            fill = self.light_color,
            font = (self.FONT, int(14.0)))

        self.canvas.create_text(
            800, 100,
            text = "Operações Aritméticas:",
            fill = self.light_color,
            font = (self.FONT, int(14.0)))

        self.canvas.create_text(
            785, 380,
            text = "Operações Lógicas:",
            fill = self.light_color,
            font = (self.FONT, int(14.0)))

        self.canvas.create_text(
            1045, 100,
            text = "Imagem Resultado:",
            fill = self.light_color,
            font = (self.FONT, int(14.0)))

        self.canvas.create_text(
            640, 520,
            text = "Arthur H Dorneles - 2022",
            fill = self.light_color,
            font = (self.FONT, int(12.0)))

        self.window.resizable(False, False)
        self.window.mainloop()

App()