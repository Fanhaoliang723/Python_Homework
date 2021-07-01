'''homwork_1：为头像加数字（图像处理），PIL库'''
from PIL import Image,ImageDraw,ImageFont
font_name = 'arial.ttf'
image_path = "F:\\Fhl\\PythonStudy\\PyProgram\\src\\image.jpg"

def change_image( font_name, image_path):

    text_font = ImageFont.truetype(font_name,55)
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    draw.text((350,3), "4", fill = (255,0,0), font=text_font)
    return image

image_new = change_image(font_name,image_path)
image_new.show()
