import numpy as np
from PIL import ImageFilter, Image, ImageDraw
#Converts an image to ascii art
#version 1 #2 second on average edge calculation a bit off 
#due to rounding
def AsciiMe(fileName, cols= 128, scale = 1 ):
    gscale = '@%#*+=-:. '
    image = Image.open(fileName).convert('L').filter(ImageFilter.EDGE_ENHANCE_MORE)

    max_width, max_height = image.size
    w = max_width/cols
    h = w/scale
    rows = int(max_height/h)
    newimg = []
    for row in range(rows):
        y1,y2 = (np.arange(row,row+2)*h).astype(int)
        newimg.append("")
        for col in range(cols):
            x1,x2 = (np.arange(col,col+2)*w).astype(int)
            newimg[row] += gscale[int((np.average(image.crop((x1, y1, x2, y2)))*9)/255)]
    return '\n'.join(newimg)
    

#version 2 0.1 second on average
def AsciiMe2(fileName,size=(512,512)):
    gscale = '@%#*+=-:. '
    image = Image.open(fileName).convert('L').filter(ImageFilter.EDGE_ENHANCE_MORE)
    image.thumbnail(size, Image.ANTIALIAS)
    normalizer = np.vectorize(lambda t: gscale[int((t * 9)/255)])
    n = normalizer(image)
    return '\n'.join([''.join(x) for x in n])

txt = AsciiMe2('Capture.PNG')
r = txt.split('\n')
x, y = len(r[0]),len(r)
img = Image.new('RGB', (x*8, y*16))
d = ImageDraw.Draw(img)
d.text((0, 0), txt, fill=(255, 255, 255))
img.save('test.png')
