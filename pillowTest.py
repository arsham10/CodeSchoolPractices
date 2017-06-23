from PIL import Image
im = Image.open("yellowish.jpg")
im2 = Image.open("modified.jpg")

pixels = im.load()
pixels2 = im2.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        print i,j
        pixels[i,j]=pixels2[im.size[0]-i-1,im.size[1]-j-1]

im.save('modifiedFliped.jpg')