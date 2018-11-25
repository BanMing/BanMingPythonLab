from PIL import Image

im=Image.open('../src/1.jpg')

#获得图片原大小
w,h=im.size

print(' Original image size: %sx%s' %(w,h))

#缩小50%
im.thumbnail(w//2,h//2)

print(' Resize image size: %sx%s' %(w//2,h//2))

im.save('../src/thumbnail.jpg')
