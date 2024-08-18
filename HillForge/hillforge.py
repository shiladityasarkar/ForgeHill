import numpy as np
import matplotlib.pyplot as pt
from PIL import Image, ImageChops, ImageEnhance
import cv2

class HillForge:
    def __init__(shila):
        pass

    def canny(shila, img, i, j):
        return cv2.Canny(np.asarray(img), i, j)

    def ela(shila, img_, quality):
        img = Image.open(img_)
        img.save('rimg.jpg', 'JPEG', quality=quality)
        rimg = Image.open('rimg.jpg')

        # pixel difference between original and resaved image
        ela_image = ImageChops.difference(img, rimg)

        # scaling factors are calculated from pixel extremas
        extrema = ela_image.getextrema()
        max_difference = max([pix[1] for pix in extrema])
        if max_difference == 0:
            max_difference = 1
        scale = 350.0 / max_difference

        # enhancing elaimage to brighten the pixels
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

        ela_image.save("ela_image.png")
        return ela_image.resize((256, 256))

    def detect(shila, img_):
        dif = {}
        for i in range(10, 110, 10):
            img = shila.canny(shila.ela(img_, i), 150, 200)
            dif[i] = len(img[img == 0]) - len(img[img == 255])
        fig, ax = pt.subplots(figsize=(4,4))
        ax.axis('off')
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        # ax.plot([80,90], [dif[80],dif[90]], color='red')
        # ax.plot([90,100], [dif[90], dif[100]], color='yellow')
        color = ['red', 'yellow']
        for i in range(10, 100, 10):
            ax.plot([i, i+10], [dif[i], dif[i+10]], color=color[int(i/10%2)])

        if dif[90]>dif[80] and dif[90]>dif[100]:
            r = True
        else:
            r = False
        return fig, r