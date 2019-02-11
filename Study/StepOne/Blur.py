from PIL import Image,ImageFilter

#打开图
img=Image.open('src/135.jpg')

#制作模糊图
img2=img.filter(ImageFilter.BLUR)

img2.save('src/blur_135.jpg')
