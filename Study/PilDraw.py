from PIL import Image,ImageFilter,ImageFont,ImageDraw

import random

#随机字母
def RandomChar():
    return chr(random.randint(65,90))

#随机颜色1
def RandomColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def RandomColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240x60
width=60*4
heigh=60

image=Image.new('RGB',(width,heigh),(255,255,255))

#创建Font对象
font=ImageFont.truetype('Arial.ttf',36)

#创建draw对象
draw=ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(heigh):
        draw.point((x,y),fill=RandomColor())

#填充文字
for t in range(4):
    draw.text((60*t+10,10),RandomChar(),font=font,fill=RandomColor2())

#模糊
image=image.filter(ImageFilter.BLUR)
image.save('../src/code.jpg')
        